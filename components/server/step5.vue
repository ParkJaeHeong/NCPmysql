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
            <li class="dropdown-item" v-for="(item, index) in serverTemplate" :key="index" @click="setTemplate(item)" v-if="item.serverNum <= data.serverNum"><a>{{item.title}}</a></li>
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
            <div v-for="(item, index) in serverList" :key="index">
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
          <!-- dep1 -->
          <draggable v-model="serverStructure" class="dragArea dep1" :options="{group:'server'}">
            <div v-for="(item, index) in serverStructure" :key="index">
              <div @click="setDeleteItem(item, [index])">
                <item :title="item.title" :delFunc="delItem"/>
              </div>
              <!-- dep2 -->
              <draggable v-model="item.children" class="dragArea dep2" :options="{group:'server'}">
                <div v-for="(item2, index2) in item.children" :key="index2" v-if="item.children[0]">
                  <div @click="setDeleteItem(item2, [index, index2])">
                    <item :title="item2.title" :delFunc="delItem"/>
                  </div>
                  <!-- dep3 -->
                  <draggable v-model="item2.children" class="dragArea dep3" :options="{group:'server'}">
                    <div v-for="(item3, index3) in item2.children" :key="index3" v-if="item2.children[0]">
                      <div @click="setDeleteItem(item3, [index, index2, index3])">
                        <item :title="item3.title" :delFunc="delItem"/>
                      </div>
                      <!-- dep4 -->
                      <draggable v-model="item3.children" class="dragArea dep4" :options="{group:'server'}">
                        <div v-for="(item4, index4) in item3.children" :key="index4"  v-if="item3.children[0]">
                          <div @click="setDeleteItem(item4, [index, index2, index3, index4])">
                            <item :title="item4.title" :delFunc="delItem"/>
                          </div>
                        </div>
                      </draggable>
                    </div>
                  </draggable>
                </div>
              </draggable>
            </div>
          </draggable>
          <!--<Tree :treeData.sync="serverStructure" />-->
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
      <button type="button" class="btn-prev btn btn-lg btn-default" @click="beforeSubmit(prevFunc, false)">이전</button>
      <button type="button" class="btn-next btn btn-lg btn-primary" @click="beforeSubmit(nextFunc, true)">다음</button>
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
  import Item from '~/components/Tree/item.vue'
  import Tree from '~/components/Tree'
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
      let init = [{
        key: '1',
        title: `${this.data.serverName}001`,
        children: []
      }]
      let temp = init
      if (this.p_serverStructure[0]) {
        temp = this.p_serverStructure
      }

      return {
        template: Item,
        lastNum: this.data.serverNum,
        initList: init,
        serverList: this.p_serverList,
        serverStructure: temp,
        settingList: this.p_settingList,
        serverTemplate: [
          { id: 1, serverNum: 2, title: '2대, M-S' },
          { id: 2, serverNum: 3, title: '3대, M-S-S' },
          { id: 3, serverNum: 3, title: "3대, M-M'-S" },
          { id: 4, serverNum: 4, title: '4대, M-S-S-S' },
          { id: 5, serverNum: 4, title: "4대, M-M'-S-S" }
        ],
        openModal: false,
        deleteInfo: null
      }
    },
    created () {
      this.resetServer()
    },
    methods: {
      beforeSubmit (Func, flag) {
        if (flag) {
          if (this.serverStructure.length > 1 || this.serverList.length !== 0) {
            this.openModal = true
            return
          }
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
            title: `${this.data.serverName}00${i}`,
            children: []
          }
          this.serverList.push(tempObject)
        }
      },
      setTemplate (item) {
        this.data.template = item.title
        this.serverList = []
        this.setServerList(item.serverNum + 1)
        if (item.id === 1) {
          this.serverStructure = [{key: 1, title: `${this.data.serverName}001`, children: [{key: 2, title: `${this.data.serverName}002`, children: []}]}]
        } else if (item.id === 2) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002`, children: [] }, { key: 3, title: `${this.data.serverName}003`, children: [] } ] } ]
        } else if (item.id === 3) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002`, children: [ { key: 3, title: `${this.data.serverName}003`, children: [] } ] } ] } ]
        } else if (item.id === 4) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002` }, { key: 3, title: `${this.data.serverName}003`, children: [] }, { key: 4, title: `${this.data.serverName}004`, children: [] } ] } ]
        } else if (item.id === 5) {
          this.serverStructure = [ { key: 1, title: `${this.data.serverName}001`, children: [ { key: 2, title: `${this.data.serverName}002`, children: [ { key: 3, title: `${this.data.serverName}003`, children: [] }, { key: 4, title: `${this.data.serverName}004`, children: [] } ] } ] } ]
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
            master: masterId
          }
        } else {
          if (this.setArrayChildren(item.children)[0]) {
            tempObject = {
              id: `${item.key}`,
              master: masterId,
              slave: this.setArrayChildren(item.children)
            }
          } else {
            tempObject = {
              id: `${item.key}`,
              master: masterId
            }
          }
        }
        this.settingList.push(tempObject)
      },
      setArrayChildren (arr) {
        let result = []
        for (let i in arr) {
          result.push(Number(arr[i].key))
        }
        return result
      },
      delItem () {
        setTimeout(() => {
          let iArr = this.deleteInfo.indexArr
          let temp = null

          // add left List
          this.addLeftList(JSON.parse(JSON.stringify(this.deleteInfo.item)))

          // remove right List
          if (iArr.length === 1) {
            temp = this.serverStructure[iArr[0]].children
            this.serverStructure.splice(iArr[0], 1)
            if (temp[0]) {
              for (let i in temp) {
                this.serverStructure.push(temp[i])
              }
            }
          } else if (iArr.length === 2) {
            temp = this.serverStructure[iArr[0]].children[iArr[1]].children
            this.serverStructure[iArr[0]].children.splice(iArr[1], 1)
            if (temp[0]) {
              for (let i in temp) {
                this.serverStructure[iArr[0]].children.push(temp[i])
              }
            }
          } else if (iArr.length === 3) {
            temp = this.serverStructure[iArr[0]].children[iArr[1]].children[iArr[2]].children
            this.serverStructure[iArr[0]].children[iArr[1]].children.splice(iArr[2], 1)
            if (temp[0]) {
              for (let i in temp) {
                this.serverStructure[iArr[0]].children[iArr[1]].children.push(temp[i])
              }
            }
          } else {
            this.serverStructure[iArr[0]].children[iArr[1]].children[iArr[2]].children.splice(iArr[3], 1)
          }
          // console.log('temp', temp)
        }, 5)
      },
      addLeftList (item) {
        item.children = []
        this.serverList.push(item)
      },
      setDeleteItem (item, indexArr) {
        this.deleteInfo = {
          item: item,
          indexArr: indexArr
        }
        // console.log(this.deleteInfo)
      }
    }
  }
</script>

<style lang="less">
  .dragArea {
    min-height: 15px;
    .dragArea {
      margin-left: 50px;
    }
  }
  .ant-tree li .ivu-tree-children {
    padding-left: 40px !important;
  }
</style>