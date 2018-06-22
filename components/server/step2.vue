<template>
  <section>

    <div class="form-horizontal">
      <h4>서버 설정</h4>
      <p class="mt-10 color-gray">서버 타입과 요금제를 선택하세요. (<span class="color-primary">·</span> 필수 입력 사항입니다.) </p>
      <hr class="mv-30" style="border-color: #000;">

      <div class="form-group">
        <label class="col-sm-3 control-label">Zone 선택</label>
        <div class="col-sm-9">
          <dropdown ref="dropdown">
            <btn type="default" class="dropdown-toggle">{{inputData.zone}}<span class="caret ml-10"></span></btn>
            <template slot="dropdown">
              <li class="dropdown-item" @click="inputData.zone = 'KR-2'"><a>KR-2</a></li>
              <li class="dropdown-item" @click="inputData.zone = 'KR-1'"><a>KR-1</a></li>
            </template>
          </dropdown>
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">스토리지 종류</label>
        <div class="col-sm-9">
          <ul class="list-inline">
            <li>
              <label class="md-check"><input type="radio" name="serverStorageType" value="SSD" v-model="inputData.storageType"> <i class="blue"></i>
                SSD
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="serverStorageType" value="HDD" v-model="inputData.storageType"> <i class="blue"></i>
                HDD
              </label>
            </li>
          </ul>
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">서버 타입</label>
        <div class="col-sm-9">
          <dropdown ref="dropdown">
            <btn type="default" class="dropdown-toggle">{{ inputData.type }}<span class="caret ml-10"></span></btn>
            <template slot="dropdown">
              <li v-for="(item, index) in types" :key="index" @click="setType(item.title)"><a role="button">{{item.title}}</a></li>
            </template>
          </dropdown>
        </div>
        <div class="col-sm-9 col-sm-push-3 mt-5">
          <dropdown ref="dropdown">
            <btn type="default" class="dropdown-toggle">{{ inputData.typeName }}<span class="caret ml-10"></span></btn>
            <template slot="dropdown">
              <li v-for="(item, index) in typeList" :key="index" @click="inputData.typeName = item.title" v-if="checkType(item)"><a role="button">{{item.title}}</a></li>
            </template>
          </dropdown>
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">요금제 선택</label>
        <div class="col-sm-9">
          <ul class="list-inline">
            <li>
              <label class="md-check"><input type="radio" name="serverFeeSystemType" value="FXSUM" v-model="inputData.FeeSystemType"> <i class="blue"></i>
                월요금제
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="serverFeeSystemType" value="MTRAT" v-model="inputData.FeeSystemType"> <i class="blue"></i>
                시간 요금제
              </label>
            </li>
            <li class="color-primary">월 34,000원 (OS 제외)</li>
          </ul>
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">서버 개수</label>
        <div class="col-sm-9 input-wrap">
          <input type="text" placeholder="최대 10개" v-model="inputData.serverNum">
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">서버 이름</label>
        <div class="col-sm-9 input-wrap">
          <input type="text" placeholder="최소 3글자, 최대 30자" v-model="inputData.serverName">
          <label check class="md-check mt-10"><input type="checkbox"><i class="blue"></i>입력하신 서버 이름으로 hostname을 설정합니다.</label>
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label">반납 보호</label>
        <div class="col-sm-9">
          <ul class="list-inline">
            <li>
              <label class="md-check"><input type="radio" name="returnProtection" value="TRUE" v-model="inputData.returnProtection"> <i class="blue"></i>
                설정
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="returnProtection" value="FALSE" v-model="inputData.returnProtection"> <i class="blue"></i>
                해제
              </label>
            </li>
          </ul>
          <p class="color-gray-light">반납 보호를 설정하면 실수로 반납하는 사고를 방지할 수 있습니다.</p>
        </div>
      </div>

    </div>
    <hr class="mt-30">

  </section>
</template>

<script>
  import {Dropdown, Btn} from 'uiv'

  export default {
    components: {
      Dropdown,
      Btn
    },
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
        types: [
          { title: '전체' },
          { title: 'Compact' },
          { title: 'Standard' },
          { title: 'High Memory' },
          { title: 'VDS' }
        ],
        typeList: [
          { type: 'Compact', title: '[Compact] vCPU 1개, 메모리 2GB, [SSD]디스크 50GB' },
          { type: 'Compact', title: '[Compact] vCPU 2개, 메모리 2GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 2개, 메모리 4GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 2개, 메모리 8GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 2개, 메모리 16GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 4개, 메모리 4GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 4개, 메모리 8GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 4개, 메모리 16GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 4개, 메모리 32GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 8개, 메모리 8GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 8개, 메모리 16GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 8개, 메모리 32GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 12개, 메모리 16GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 12개, 메모리 32GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 16개, 메모리 16GB, [SSD]디스크 50GB' },
          { type: 'Standard', title: '[Standard] vCPU 16개, 메모리 32GB, [SSD]디스크 50GB' },
          { type: 'High Memory', title: '[High-Memory] vCPU 8개, 메모리 64GB, [SSD]디스크 50GB' },
          { type: 'High Memory', title: '[High-Memory] vCPU 16개, 메모리 64GB, [SSD]디스크 50GB' },
          { type: 'High Memory', title: '[High-Memory] vCPU 16개, 메모리 128GB, [SSD]디스크 50GB' },
          { type: 'High Memory', title: '[High-Memory] vCPU 32개, 메모리 128GB, [SSD]디스크 50GB' },
          { type: 'High Memory', title: '[High-Memory] vCPU 32개, 메모리 256GB, [SSD]디스크 50GB' },
          { type: 'VDS', title: '[VDS] vCPU 20개, 메모리 80GB, [SSD]디스크 1000GB (기본50GB/추가950GB)' },
          { type: 'VDS', title: '[VDS] vCPU 20개, 메모리 80GB, [SSD]디스크 2000GB (기본50GB/추가1950GB)' },
          { type: 'VDS', title: '[VDS] vCPU 32개, 메모리 122GB, [SSD]디스크 1000GB (기본50GB/추가950GB)' },
          { type: 'VDS', title: '[VDS] vCPU 32개, 메모리 122GB, [SSD]디스크 2000GB (기본50GB/추가1950GB)' },
          { type: 'VDS', title: '[VDS] vCPU 32개, 메모리 244GB, [SSD]디스크 1000GB (기본50GB/추가950GB)' },
          { type: 'VDS', title: '[VDS] vCPU 32개, 메모리 244GB, [SSD]디스크 2000GB (기본50GB/추가1950GB)' }
        ]
      }
    },
    methods: {
      setServerImage (item) {
        this.inputData.name = item.title
        this.inputData.description = item.description
        this.nextFunc()
      },
      setType (title) {
        this.inputData.type = title
        this.inputData.typeName = '선택해주세요'
      },
      checkType (item) {
        if (this.inputData.type === '전체') return true
        if (this.inputData.type === item.type) return true
        // console.log(this.inputData.type, item.type)
        return false
      }
    }
  }
</script>
