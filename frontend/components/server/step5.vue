<template>
  <section>

    step5

  </section>
</template>

<script>
export default {
  props: {
    inputData: {
      type: Object
    }
  },
  data() {
    return {
      options: {
        sortKey: 'order',
        parentKey: 'parentId',
        childrenKey: "children",
      },
      treeData: [
        {
          id: 1,
          label: 'id: 1',
          order: 0,
          parentId: null,
          children: []
        }
      ]
    }
  },
  methods: {
    getdata(){
      this.formated = this.$refs.tree.reformatData();
    }
  }
}
</script>

