<template>
  <section>

    <h4>복제 환경 설정</h4>
    <p class="mt-10 color-gray">서버 복제 환경을 설정합니다.</p>
    <hr class="mv-30" style="border-color: #000;">

    <div class="row">
      <div class="col-sm-12 mb-20 text-left">
        <dropdown ref="dropdown">
          <btn type="default" class="dropdown-toggle">{{ data.template }}<span class="caret ml-10"></span></btn>
          <template slot="dropdown">
            <li class="dropdown-item" v-for="item in serverTemplate" @click="setTemplate(item)" v-if="item.serverNum <= data.serverNum"><a>{{item.title}}</a></li>
          </template>
        </dropdown>
        <button type="button" @click="addServer" class="btn btn-primary ml-10">서버 추가</button>
        <button type="button" @click="deleteServer" class="btn btn-default ml-10">서버 삭제</button>
        <button type="button" @click="resetServer" class="btn btn-gray ml-10">복제 환경 초기화</button>
        <!--<button type="button" @click="setSettingList(serverStructure[0], null)" class="btn btn-primary ml-10">셋팅 리스트 만들기!</button>-->
      </div>

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

      <!--<div class="col-xs-12 mt-20">-->
        <!--serverList:-->
        <!--{{serverList}}-->
      <!--</div>-->
      <!--<div class="col-xs-12 mt-20">-->
        <!--serverStructure:-->
        <!--{{serverStructure}}-->
      <!--</div>-->
      <!--<div class="col-xs-12 mt-20">-->
        <!--settingList:-->
        <!--{{settingList}}-->
      <!--</div>-->
    </div>
    <hr class="mv-40">

    <div class="text-center">
      <button type="button" class="btn-prev btn btn-lg btn-default" @click="prevFunc">이전</button>
      <button type="button" class="btn-next btn btn-lg btn-primary" @click="beforeSubmit(nextFunc)">다음</button>
    </div>

    <modal v-model="openModal" title="설정 미완료" size="sm" :header="false" :footer="false">
      <div class="pv-20">
        <h5 class="color-primary text-center">복제 환경 설정을 완료해주세요.</h5>
        <p class="text-center">(참고로, 최상단 서버는 1개여야 합니다.)</p>
      </div>
    </modal>

  </section>
</template>

<script>
  import Item from '~/components/TreeItem.vue'
  import Tree from 'vue-draggable-tree'
  import draggable from 'vuedraggable'
  import {Dropdown, Btn, Modal} from 'uiv'

  export default {
    components: {
      Tree,
      Item,
      draggable,
      Dropdown,
      Btn,
      Modal
    },
    props: {
      data: {
        type: Object
      },
      p_serverList: {
        type: Array
      },
      p_serverStructure: {
        type: Array
      },
      p_settingList: {
        type: Array
      },
      nextFunc: {
        type: Function
      },
      prevFunc: {
        type: Function
      }
    },
    data () {
      return {
        template: Item,
        lastNum: this.data.serverNum,
        initList: [{
          key: '1',
          title: `${this.data.serverName}001`
        }],
        serverList: this.p_serverList,
        serverStructure: this.p_serverStructure,
        settingList: this.p_settingList,
        newServerStructure: [{
          key: '1',
          title: `${this.data.serverName}001`
        }],
        serverTemplate: [
          { id: 1, serverNum: 2, title: '2대, M-S' },
          { id: 2, serverNum: 3, title: '3대, M-S-S' },
          { id: 3, serverNum: 3, title: "3대, M-M'-S" },
          { id: 4, serverNum: 4, title: '4대, M-S-S-S' },
          { id: 5, serverNum: 4, title: "4대, M-M'-S-S" }
        ],
        openModal: false
      }
    },
    mounted () {
      this.resetServer()
    },
    methods: {
      beforeSubmit (Func) {
        if (this.serverStructure.length > 1 || this.serverList.length !== 0) {
          this.openModal = true
          return
        }
        this.settingList = []
        this.setSettingList(this.serverStructure[0], null)
        this.$emit('update:p_serverList', this.serverList)
        this.$emit('update:p_serverStructure', this.serverStructure)
        this.$emit('update:p_settingList', this.settingList)
        Func()
      },
      setServerList (startNum) {
        for (let i = startNum; i <= this.data.serverNum; i++) {
          let tempObject = {
            key: i,
            title: `${this.data.serverName}00${i}`
          }
          this.serverList.push(tempObject)
        }
      },
      setTemplate (item) {
        this.data.template = item.title
        this.serverList = []
        this.setServerList(item.serverNum + 1)
        if (item.id === 1) {
          this.serverStructure = [{key: 1, title: `${this.data.serverName}001`, children: [{key: 2, title: `${this.data.serverName}002`}]}]
        } else if (item.id === 2) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002` }, { key: 3, title: `${this.data.serverName}003` } ] } ]
        } else if (item.id === 3) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002`, children: [ { key: 3, title: `${this.data.serverName}003` } ] } ] } ]
        } else if (item.id === 4) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002` }, { key: 3, title: `${this.data.serverName}003` }, { key: 4, title: `${this.data.serverName}004` } ] } ]
        } else if (item.id === 5) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002`, children: [ { key: 3, title: `${this.data.serverName}003` }, { key: 4, title: `${this.data.serverName}004` } ] } ] } ]
        }
      },
      addServer () {
        if (this.data.serverNum >= 8) return
        this.data.serverNum++
        let tempObject = {
          key: this.data.serverNum,
          title: `${this.data.serverName}00${this.data.serverNum}`
        }
        this.serverList.push(tempObject)
      },
      deleteServer () {
        if (this.data.serverNum <= 1) return
        for (let i in this.serverList) {
          if (this.serverList[i].key === this.data.serverNum) {
            this.serverList.splice(i, 1)
            this.data.serverNum--
          }
        }
        for (let i in this.serverStructure) {
          if (this.serverStructure[i].key === this.data.serverNum) {
            this.serverStructure.splice(i, 1)
            this.data.serverNum--
          }
        }
      },
      resetServer () {
        this.serverStructure = JSON.parse(JSON.stringify(this.initList))
        this.serverList = []
        this.setServerList(2)
        this.data.template = '템플릿 선택'
      },
      setSettingList (Object, key) {
        this.pushSettingList(Object, key)
        if (Object.children !== []) {
          for (let i in Object.children) {
            this.setSettingList(Object.children[i], Object.key)
          }
        }
      },
      pushSettingList (item, masterId) {
        let tempObject = null
        if (masterId === null) {
          tempObject = {
            id: `${item.key}`,
            master: 'Null'
          }
        } else {
          if (this.setArrayChildren(item.children)[0]) {
            tempObject = {
              id: `${item.key}`,
              master: `${masterId}`,
              slave: this.setArrayChildren(item.children)
            }
          } else {
            tempObject = {
              id: `${item.key}`,
              master: `${masterId}`
            }
          }
        }
        this.settingList.push(tempObject)
      },
      setArrayChildren (arr) {
        let result = []
        for (let i in arr) {
          result.push(`${arr[i].key}`)
        }
        return result
      }
    }
  }
</script>

<style lang="less">
  .ant-tree li .ivu-tree-children {
    padding-left: 40px !important;
  }
</style>
