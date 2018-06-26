<template>
  <div class="tree">
    <draggable v-model="treeList" class="dragArea" :options="{group:'server'}" @update="$emit('update:treeData', treeList)">
      <div v-for="(item, index) in treeList" :key="index">
        <item :title="item.title"/>
        <tree :treeData="item.children" v-if="item.children && item.children.length"/>  
      </div>
    </draggable>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
import Item from './item'

export default {
  name: 'tree',
  components: {
    draggable,
    Item
  },
  props: {
    treeData: Array
  },
  data () {
    return {
      // treeList: this.treeData
    }
  },
  computed: {
    treeList: function () {
      return this.treeData
    }
  }
}
</script>

<style>
.tree-list ul {
  padding-left: 16px;
  margin: 6px 0;
}
</style>