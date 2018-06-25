<template>
  <section id="TreeItem" class="pv-5">
    <ul class="list-unstyled list-item p-0">
      <li><img src="/img/server.gif" alt="" class="img-server"></li>
      <li class="title">{{title}}</li>
      <li><button type="button" class="btn-delete" v-if="isDeleteBtn"><i class="glyphicon glyphicon-remove"></i></button></li>
    </ul>
  </section>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        default: ''
      },
      isDeleteBtn: {
        type: Boolean,
        default: true
      }
    },
    methods: {}
  }
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";

  #TreeItem {
    li {
      display: inline-block;
      padding: 0;
      & + li {
        margin-left: 10px;
      }
    }

    .img-server {
      width: 50px;
      height: auto;
    }

    .title {
      font-size: 15px;
      font-weight: 600;
      color: @gray-light;
    }

    .btn-delete {
      border: none;
      color: lighten(@brand-primary, 13.5%);
      background-color: transparent;

      &:hover,
      &:focus {
        color: @brand-primary;
        outline: none;
      }
    }
  }
</style>