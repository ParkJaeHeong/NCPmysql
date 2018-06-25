<template>
  <section id="main" class="container">

    메인 페이지입니다.
    <nuxt-link :to="'/server'">서버</nuxt-link>

  </section>
</template>

<script>
  export default {
    async asyncData ({ redirect }) {
      // redirect('/server')
    }
  }
</script>
