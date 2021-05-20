<template>
  <div id="song-list">
    <p v-if="songs.length < 1" class="empty-table">No Songs</p>
    <table v-else>
      <thead>
        <tr>
          <th>Title</th>
          <th>Project</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="song in songs" :key="song.id">
          <td v-if="editing === song.id">
            <input type="text" v-model="song.title" />
          </td>
          <td v-else>{{ song.title }}</td>
          <td v-if="editing === song.id">
            <input type="text" v-model="song.project_name" />
          </td>
          <td v-else>{{ song.project_name }}</td>
          <td v-if="editing === song.id">
            <button @click="editSong(song.id)">Save</button>
            <button class="muted-button" @click="editing = null">Cancel</button>
          </td>
          <td v-else>
            <button @click="editMode(song)">Edit</button>
            <button @click="$emit('delete:song', song.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'song-list',
  props: {
    songs: Array,
  },
  data() {
    return {
      editing: null,
    }
  },
  methods: {
    editMode(song) {
      this.cachedSong = Object.assign({}, song)
      this.editing = song.id
    },

    cancelEdit(song) {
      Object.assign(song, this.cachedSong)
      this.editing = null;
    },

    editSong(song) {
      if (song.title === '' || song.project_name === '') return
      this.$emit('edit:song', song.id, song)
      this.editing = null
    },
  }
}
</script>

<style scoped>
  button {
    margin: 0. 0.5rem 0 0;
  }
</style>
