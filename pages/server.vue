<template>
  <section id="server" class="container">

    <header class="text-center pv-md">
      <h2>서버 생성</h2>
      <p class="mt-10 color-gray-light">새로운 VM 서버를 생성합니다</p>
    </header>

    <div class="row">
      <div class="col-sm-8 col-sm-push-2">
        <StepMark class="mb-md"
                  :titles="['서버 이미지 선택', '서버 설정', '인증키 설정', '네트워크 접근 설정', '복제 환경 설정', '최종 확인']"
                  :stepActive="stepNum" />
      </div>
      <div class="col-sm-12 col-md-10 col-md-push-1">

        <step1 :inputData="inputData.serverImg" :nextFunc="goNext" v-if="stepNum === 1"/>
        <step2 :inputData="inputData.server" :nextFunc="goNext" v-if="stepNum === 2"/>
        <step3 :inputData="inputData.authentication" v-if="stepNum === 3"/>
        <step4 :inputData="inputData.setUpAcg" v-if="stepNum === 4"/>
        <step5 :data="inputData.server" v-if="stepNum === 5"/>
        <step6 :data="inputData" v-if="stepNum === 6"/>

      </div>
    </div>

    <div class="text-center mt-40">
      <template v-if="stepNum !== 1">
        <button type="button" class="btn-prev btn btn-lg btn-default" @click="stepNum--" v-if="stepNum !== 1">이전</button>
        <button type="button" class="btn-next btn btn-lg btn-primary" @click="stepNum++" v-if="stepNum !== maxStepNum">다음</button>
      </template>
      <template v-if="stepNum === maxStepNum">
        <nuxt-link to="/" class="btn-next btn btn-lg btn-primary">서버 생성</nuxt-link>
      </template>
    </div>

  </section>
</template>

<script>
  import StepMark from '~/components/StepMark'
  import step1 from '~/components/server/step1.vue'
  import step2 from '~/components/server/step2.vue'
  import step3 from '~/components/server/step3.vue'
  import step4 from '~/components/server/step4.vue'
  import step5 from '~/components/server/step5.vue'
  import step6 from '~/components/server/step6.vue'

  export default {
    components: {
      StepMark,
      step1,
      step2,
      step3,
      step4,
      step5,
      step6
    },
    data () {
      return {
        stepNum: 6,
        maxStepNum: 6,
        inputData: {
          serverImg: {
            name: 'centos-7.3-64', // null
            description: 'CentOS 7.3 (64-bit)', // null
            bootingDiskSize: 53687091200,
            osType: 'os',
            osDetailType: 'ALL',
            dbmsOsDetailType: 'ALL'
          },
          server: {
            storageType: 'SSD',
            FeeSystemType: 'FXSUM',
            serverNum: 5,
            serverName: 'abc',
            returnProtection: 'TRUE',
            zone: 'KR-2',
            type: '전체',
            typeName: '선택해주세요'
          },
          authentication: {
            authentication: 'sel',
            name: '선택해주세요',
            addName: null,
            list: []
          },
          setUpAcg: {
            type: 'sel',
            name: '선택해주세요'
          }
        }
      }
    },
    methods: {
      goNext () {
        this.stepNum++
      }
    }
  }
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";

  .btn-prev,
  .btn-next {
    font-size: 14px;
    width: 200px;
  }

  .btn {
    @media (max-width: @screen-xs-max) {
      width: 100%;
    }
    & + .btn {
      @media (max-width: @screen-xs-max) {
        margin-top: 10px;
      }
      @media (min-width: @screen-sm-min) {
        margin-left: 10px;
      }
    }
  }
</style>
