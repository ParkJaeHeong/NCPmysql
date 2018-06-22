<template>
  <section id="stepMark">

    <ul class="list-step list-unstyled" :class="{ 'text-hidden': !isText }">
      <!-- text -->
      <template v-if="titles[0]">
        <li v-for="(title, index) in titles" :key="index" :class="{ 'active': index + 1 <= stepActive }">
          <i class="dot"></i><span class="text">{{ title }}</span>
        </li>
      </template>
      <!-- step -->
      <template v-else>
        <li v-for="n in maxNum" :key="index" :class="{ 'active': n <= stepActive }">
          <i class="dot"></i><span class="text">STEP{{n}}</span>
        </li>
      </template>
    </ul>

  </section>
</template>

<script>
  export default {
    props: {
      maxNum: {
        type: Number,
        default: 1
      },
      stepActive: {
        type: Number,
        default: 1
      },
      titles: {
        type: Array,
        default: function () {
          return []
        }
      },
      isText: {
        type: Boolean,
        default: true
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";
  @import "~assets/less/bootstrap/mixins/vendor-prefixes.less";

  #stepMark {
    .list-step {
      display: table;
      table-layout: fixed;
      width: 100%;

      > li {
        display: table-cell;
        position: relative;
        text-align: center;
        line-height: 1;
        height: 40px;

        @r: 7px;

        .dot {
          position: relative;
          z-index: 30;
          display: inline-block;
          width: (@r*2);
          height: (@r*2);
          border-radius: 50%;
          background-color: #ccc;
        }

        .text {
          position: absolute;
          top: 25px;
          left: 0;
          width: 100%;
          font-size: 13px;
          color: #888;
        }

        // line
        & + li {
          &:before,
          &:after {
            position: absolute;
            content: '';
            display: block;
            top: @r - 1;
            left: -50%;
            width: 100%;
            height: 1px;
          }

          &:before {
            z-index: 10;
            background-color: #f0f0f0;
          }

          &:after {
            width: 0;
            z-index: 20;
            background-color: @brand-primary;
            .transition(0.3s);
          }
        }

        &.active {
          .dot {
            &:after {
              font-family: "Glyphicons Halflings";
              content: '\E013';
              font-size: 14px;
              font-style: normal;
              color: @brand-primary;
              background-color: #fff;
            }
          }

          .text {
            color: @brand-primary;
          }

          // line
          &:after {
            width: 100%;
            z-index: 20;
            background-color: @brand-primary;
          }
        }
      }
    }
  }
</style>