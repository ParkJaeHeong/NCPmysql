<template>
  <section>

    <h4>최종 확인</h4>
    <p class="mt-10 color-gray">[서버 생성] 버튼을 클릭하면 서버가 생성됩니다.</p>
    <hr class="mv-30" style="border-color: #000;">

    <!--<h6>서버 이미지</h6>-->
    <!--<div class="card p-20 mt-15">-->
      <!--<ul class="list-unstyled row">-->
        <!--<li class="col-xs-4 col-sm-2">서버 이미지 이름</li>-->
        <!--<li class="col-xs-8 col-sm-4 color-gray-light">{{data.serverImg.name}}</li>-->
        <!--<li class="col-xs-4 col-sm-2">서버 이미지 설명</li>-->
        <!--<li class="col-xs-8 col-sm-4 color-gray-light">{{data.serverImg.description}}</li>-->
      <!--</ul>-->
    <!--</div>-->

    <h6 class="mt-40">서버</h6>
    <div class="card p-20 mt-15">
      <ul class="list-unstyled row">
        <li class="col-xs-4 col-sm-2">스토리지 종류</li>
        <li class="col-xs-8 col-sm-4 color-gray-light">{{data.server.storageType}}&nbsp;</li>
        <li class="col-xs-4 col-sm-2">서버 이름</li>
        <li class="col-xs-8 col-sm-4 color-gray-light">{{data.server.serverName}}&nbsp;</li>
        <li class="col-xs-4 col-sm-2 pt-10">서버 타입</li>
        <li class="col-xs-8 col-sm-4 pt-10 color-gray-light">{{data.server.typeName}}&nbsp;</li>
        <li class="col-xs-4 col-sm-2 pt-10">요금제</li>
        <li class="col-xs-8 col-sm-4 pt-10 color-gray-light">{{data.server.FeeSystemType === 'FXSUM' ? '월요금제' : '시간 요금제'}}</li>
        <li class="col-xs-4 col-sm-2 pt-10">Zone</li>
        <li class="col-xs-8 col-sm-4 pt-10 color-gray-light">{{data.server.zone}}&nbsp;</li>
        <li class="col-xs-4 col-sm-2 pt-10">반납 보호</li>
        <li class="col-xs-8 col-sm-4 pt-10 color-gray-light">{{data.server.returnProtection === 'TRUE' ? '설정' : '해제'}}</li>
      </ul>
    </div>

    <!--<h6 class="mt-40">인증키</h6>-->
    <!--<div class="card p-20 mt-15">-->
      <!--<ul class="list-unstyled row">-->
        <!--<li class="col-xs-4 col-sm-2">인증키 이름</li>-->
        <!--<li class="col-xs-8 col-sm-4 color-gray-light">{{data.authentication.name}}</li>-->
      <!--</ul>-->
    <!--</div>-->

    <!--<h6 class="mt-40">Access Control Group</h6>-->
    <!--<div class="card p-20 mt-15">-->
      <!--<ul class="list-unstyled row">-->
        <!--<li class="col-xs-4 col-sm-2">ACG 이름</li>-->
        <!--<li class="col-xs-8 col-sm-4 color-gray-light">{{data.setUpAcg.name}}</li>-->
      <!--</ul>-->
    <!--</div>-->

    <h6 class="mt-40">복제 환경 설정</h6>
    <div class="card p-20 mt-15">
      <ul class="list-unstyled row">
        <li class="col-xs-4 col-sm-2 col-lg-2">복제 환경 구성</li>
        <li class="col-xs-8 col-sm-10 col-lg-2 color-gray-light">{{data.server.template}}</li>
        <li class="col-xs-4 col-sm-2 col-lg-2">서버 구성</li>
        <li class="col-xs-8 col-sm-10 col-lg-6 color-gray-light">{{getSettingStructure()}}</li>
      </ul>
    </div>
    <hr class="mv-40">

    <div class="text-center">
      <button type="button" class="btn-prev btn btn-lg btn-default" @click="prevFunc">이전</button>
      <button type="button" class="btn-next btn btn-lg btn-primary" @click="nextFunc">서버 생성</button>
    </div>

  </section>
</template>

<script>
export default {
  props: {
    data: {
      type: Object
    },
    settingList: {
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
      settingStructure: ''
    }
  },
  mounted () {
    // this.getSettingStructure()
  },
  methods: {
    getSettingStructure () {
      let temp = ''
      let arr = this.settingList
      for (let i in arr) {
        if (arr[i].master === null) {
          temp += 'Master - '
        } else if (arr[i].slave) {
          temp += ', Dual - '
        } else {
          temp += ', Slave - '
        }
        temp += `${this.data.server.serverName}00${arr[i].id}`
      }
      return temp
    }
  }
}
</script>

