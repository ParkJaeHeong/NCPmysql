<template>
  <section>

    step6

  </section>
</template>

<script>
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
    }
  }
}
</script>

