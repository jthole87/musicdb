<template>
  <div id="song-form">
    <form @submit.prevent="handleSubmit">
      <label>Song Title</label>
      <input
        ref="first"
        type="text"
        :class="{ 'has-error': submitting && invalidTitle }"
        v-model="song.title"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <label>Project Name</label>
      <input
        type="text"
        :class="{ 'has-error': submitting && invalidProject }"
        v-model="song.project_name" 
        @focus="clearStatus"
      />
      <label>Author</label>
      <input
        type="text"
        :class="{ 'has-error': submitting && invalidAuthor }"
        v-model="song.author"
        @focus="clearStatus"
      />
      <p v-if="error && submitting" class="error-message">
        !Please fill out all required fileds.
      </p>
      <p v-if="success" class="success-message"> !Song Added. >
      </p>

      <button>Add Song</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'song-form',
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      song: {
        title: '',
        project_name: '',
        author: '',
      },
    }
  },

  methods: {
    handleSubmit() {
      this.submitting = true
      this.clearStatus()

      if (this.invalidTitle || this.invalidProject || this.invalidAuthor) {
        this.error = true
        return
      }

      this.$emit('add:song', this.song)
      this.$refs.first.focus()
      this.employee = {
        name: '',
        email: '',
      }

      this.error = false
      this.success = true
      this.submitting = false
    },

    clearStatus() {
      this.success = false
      this.error = false
    }
  },

  computed: {
    invalidTitle() {
      return this.song.title === ''
    },

    invalidProject() {
      return this.song.project_name === ''
    },

    invalidAuthor() {
      return this.song.author === ''
    },
  }
}
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }

  [class*='-message'] {
    font-weight: 500;
  }

  .error-message {
    color: #d33c40;
  }

  .success-message {
    color: #32a95d;
  }
</style>
