<template>
  <div class="app">
    <my-header/>
    <div class="main container">
      <section class="panal card p-40 mv-md">   
        <nuxt/>
      </section>
    </div>
    <my-footer/>
  </div>
</template>

<script>
import MyFooter from '~/components/Footer.vue'
import MyHeader from '~/components/Header.vue'

export default {
  components: {
    MyFooter,
    MyHeader
  }
}
</script>

<style lang="less" scoped>
  .app {
    background-color: #f6f7f8;
  }
</style>
