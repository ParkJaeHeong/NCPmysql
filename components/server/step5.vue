<template>
  <section>

    <h4>복제 환경 설정</h4>
    <p class="mt-10 color-gray">멘트</p>
    <hr class="mv-30" style="border-color: #000;">

    <div class="row">
      <div class="col-sm-4">
        <div class="card p-20">
          <draggable v-model="serverList" class="dragArea" :options="{group:'server'}">
            <div v-for="(item, index) in serverList" :key="index" class="m-10">
              <item :title="item.title" :isDeleteBtn="false"/>
            </div>
          </draggable>
          <div v-if="serverList.length === 0">
            이동할 서버가 없습니다.
          </div>
        </div>
      </div>

      <div class="col-sm-8">
        <div class="card p-20">
          <draggable v-model="serverStructure" class="dragArea" :options="{group:'server'}">
            <Tree draggable
                  v-model="serverStructure"
                  :template="template"/>
          </draggable>
        </div>
      </div>

      <div class="col-xs-12 mt-20">
        serverList:
        {{serverList}}
      </div>
      <div class="col-xs-12 mt-20">
        serverStructure:
        {{serverStructure}}
      </div>
    </div>

  </section>
</template>

<script>
  import Item from '~/components/TreeItem.vue'
  import Tree from 'vue-draggable-tree'
  import draggable from 'vuedraggable'

  export default {
    components: {
      Tree,
      Item,
      draggable
    },
    props: {
      data: {
        type: Object
      }
    },
    data () {
      return {
        template: Item,
        serverStructure: [
          {
            key: '1',
            title: `${this.data.serverName}_001`
          }
        ],
        serverList: []
      }
    },
    mounted () {
      this.setServerList()
    },
    methods: {
      setServerList () {
        console.log('setServerList', this.data.serverNum)
        for (let i = 2; i <= this.data.serverNum; i++) {
          let tempObject = {
            key: i,
            title: `${this.data.serverName}_${this.setNumThree(i)}`
          }
          this.serverList.push(tempObject)
        }
      },
      setNumThree (num) {
        if (Number(num) >= 10) return `0${num}`
        else return `00${num}`
      }
    }
  }
</script>

<style lang="less">
  .ant-tree li .ivu-tree-children {
    padding-left: 40px !important;
  }
</style>