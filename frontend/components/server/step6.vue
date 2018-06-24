<template>
  <section>

    step6
    <button @click="createServer">서버 생성</button>
  </section>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  props: {
    inputData: {
      type: Object
    },
    nextFunc: {
      type: Function
    }
  },
  data () {
    return {
    }
  },
  methods: {
    setServerImage (item) {
      this.nextFunc()
    },
    async createServer() {
      const users = await axios.post('/api/server');
      console.log(users);
    },
  }
}
</script>

