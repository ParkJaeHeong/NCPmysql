<template>
  <section id="server" class="container">

    <header class="text-center pv-md">
      <h2>서버 생성</h2>
      <p class="mt-10 color-gray-light">새로운 VM 서버를 생성합니다</p>
    </header>

    <div class="row">
      <div class="col-sm-8 col-sm-push-2">
        <StepMark class="mb-md"
                  :titles="['서버 설정', '복제 환경 설정', '최종 확인']"
                  :stepActive="stepNum" />
        <!--<StepMark class="mb-md"-->
                  <!--:titles="['서버 이미지 선택', '서버 설정', '인증키 설정', '네트워크 접근 설정', '복제 환경 설정', '최종 확인']"-->
                  <!--:stepActive="stepNum" />-->
      </div>
      <div class="col-sm-12 col-md-10 col-md-push-1">
        <!--<step1 :inputData="inputData.serverImg" :nextFunc="goNext" v-if="stepNum === 1"/>-->
        <step2 :inputData="inputData.server" :nextFunc="goNext" :prevFunc="goPrev" v-if="stepNum === 1"/>
        <!--<step3 :inputData="inputData.authentication" :nextFunc="goNext" :prevFunc="goPrev" v-if="stepNum === 3"/>-->
        <!--<step4 :inputData="inputData.setUpAcg" :nextFunc="goNext" :prevFunc="goPrev" v-if="stepNum === 4"/>-->
        <step5 :data="inputData.server" v-bind.sync="setting" :nextFunc="goNext" :prevFunc="goPrev" v-if="stepNum === 2"/>
        <step6 :data="inputData" :settingList="setting.p_settingList" :nextFunc="createServer" :prevFunc="goPrev" v-if="stepNum === 3"/>
      </div>
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
        stepNum: 1,
        maxStepNum: 3,
        inputData: {
          serverImg: {
            name: null,
            description: null,
            bootingDiskSize: '53687091200',
            osType: 'os',
            osDetailType: 'ALL',
            dbmsOsDetailType: 'ALL'
          },
          server: {
            zone: 'KR-2',
            storageType: 'SSD',
            FeeSystemType: 'FXSUM',
            serverNum: 1,
            serverName: null,
            cloneId: null,
            clonePw: null,
            returnProtection: 'TRUE',
            type: '전체',
            typeName: '[Compact] vCPU 1개, 메모리 2GB, [SSD]디스크 50GB',
            template: '템플릿 선택'
          },
          authentication: {
            authentication: 'sel',
            name: '선택해주세요',
            addName: '',
            list: []
          },
          setUpAcg: {
            type: 'sel',
            name: '선택해주세요'
          }
        },
        setting: {
          p_serverList: [],
          p_serverStructure: [],
          p_settingList: []
        }
      }
    },
    methods: {
      goNext () {
        this.stepNum++
      },
      goPrev () {
        this.stepNum--
      },
      createServer () {
        console.log('createServer')
        let temp = {
          setting: this.setting.p_settingList,
          dbUser: {
            id: this.inputData.server.cloneId,
            pw: this.inputData.server.clonePw
          }
        }
        this.axios.post('/api/server', temp).then((resp) => {
          console.log(resp)
        }).catch((err) => {
          console.log(err)
        })
      }
    }
  }
</script>

<style lang="less">
  @import "~assets/less/bootstrap/variables.less";

  input.err {
    border: 1px solid @brand-danger;
  }
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
