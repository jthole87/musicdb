<template>
  <div id="app" class="small-container">
    <h1>Songs</h1>

    <song-form @add:song="addSong" />
    <song-list 
      v-bind:songs="songs" 
      @delete:song="deleteSong" 
      @edit:song="editSong"
    />
  </div>
</template>

<script>
import SongList from '@/components/SongList.vue'
import SongForm from '@/components/SongForm.vue'

export default {
  name: 'App',
  components: {
    SongList,
    SongForm,
  },
  methods: {
    async getProjectName(song) {
      try {
        const response = await fetch(song.project)
        const data = await response.json()
        song.project_name = data.name
      } catch (error) {
        console.error(error)
      }
    },

    async getSongs() {
      try {
        const response = await fetch('http://10.0.0.18:8000/api/songs/')
        const data = await response.json()
        for (const song of data) {
          this.getProjectName(song)
        }
        this.songs = data
      } catch (error) {
        console.error(error)
      }
    },

    async addSong(song) {
      try {
        const response = await fetch('http://10.0.0.18:8000/api/songs/', {
          method: "POST",
          body: JSON.stringify(song),
          headers:{ 'Content-type': 'application/json; charset=UTF-8' },
        })
      const data = await response.json()
      this.songs = [...this.songs, data]
      } catch (error) {
        console.error(error)
      }
    },

    async deleteSong(id) {
      try {
        await fetch(`http://10.0.0.18:8000/api/songs/${id}/`, {
          method: "DELETE"
        });
        this.songs = this.songs.filter(song => song.id !== id);
      } catch (error) {
        console.error(error);
      }
    },

    async editSong(id, updatedSong) {
      try {
        const response = await fetch(`http://10.0.0.18:8000/api/songs/${id}`, {
          method: 'PUT',
          body: JSON.stringify(updatedSong),
          headers: { 'Content-type': 'application/json; charset=UTF-8' },
        })
        const data = await response.json()
        this.songs = this.songs.map(song => (song.id === id ? data: song))
      } catch (error) {
        console.error(error)
    }
    }
  },
  data() {
    return {
      songs : [],
    }
  },
  
  mounted() {
    this.getSongs()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
