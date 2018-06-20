<template>
  <section>

    <div class="form-horizontal">
      <h4>서버 설정</h4>
      <p class="mt-10 color-gray">서버 타입과 요금제를 선택하세요. (<span class="color-primary">·</span> 필수 입력 사항입니다.) </p>
      <hr class="mv-30" style="border-color: #000;">

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">Zone 선택</label>
        <div class="col-sm-9">
          <dropdown ref="dropdown">
            <btn type="primary" class="dropdown-toggle">Dropdown <span class="caret"></span></btn>
            <template slot="dropdown">
              <li><a role="button">Action</a></li>
            </template>
          </dropdown>
        </div>
      </div>

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">스토리지 종류</label>
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
        <label for="username" class="col-sm-3 control-label">서버 타입</label>
        <div class="col-sm-9">
          <dropdown ref="dropdown">
            <btn type="primary" class="dropdown-toggle">Dropdown <span class="caret"></span></btn>
            <template slot="dropdown">
              <li><a role="button">Action</a></li>
            </template>
          </dropdown>
        </div>
      </div>

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">요금제 선택</label>
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
        <label for="username" class="col-sm-3 control-label">서버 개수</label>
        <div class="col-sm-9 input-wrap">
          <input type="text" placeholder="최대 10개" v-model="inputData.serverNum">
        </div>
      </div>

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">서버 이름</label>
        <div class="col-sm-9 input-wrap">
          <input type="text" placeholder="최소 3글자, 최대 30자" v-model="inputData.serverName">
          <label check class="md-check mt-10"><input type="checkbox"><i class="blue"></i>입력하신 서버 이름으로 hostname을 설정합니다.</label>
        </div>
      </div>

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">반납 보호</label>
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
import { Dropdown } from 'uiv'

export default {
  components: {
    Dropdown
  },
  props: {
    inputData: {
      type: Object
    },
    selected: {
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
      this.inputData.name = item.title
      this.inputData.description = item.description
      this.nextFunc()
    }
  }
}
</script>
