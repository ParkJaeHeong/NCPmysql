<template>
  <section id="server" class="container">

    <header class="text-center pv-md">
      <h2>서버 생성</h2>
      <p class="mt-10 color-gray-light">새로운 VM 서버를 생성합니다</p>
    </header>
    
    <div class="row">
      <div class="col-sm-12 col-md-10 col-md-push-1">

        <step1 :inputData="inputData.serverImg" :selected="selected.serverImg" :nextFunc="goNext" v-if="stepNum === 1"/>
        <step2 :inputData="inputData.server" :nextFunc="goNext" v-if="stepNum === 2"/>
        <step3 :inputData="inputData.authentication" v-if="stepNum === 3"/>
        <step4 :inputData="inputData.setUpAcg" v-if="stepNum === 4"/>
        <step5 v-if="stepNum === 5"/>
        <step6 v-if="stepNum === 6"/>

      </div>
    </div>

    <div class="text-center mt-40">
      <template v-if="stepNum !== 1 && stepNum !== maxStepNum">
        <button type="button" class="btn-prev btn btn-lg btn-default" @click="stepNum--" v-if="stepNum !== 1">이전</button>
        <button type="button" class="btn-next btn btn-lg btn-primary" @click="stepNum++">다음</button>
      </template>
      <template v-if="stepNum === maxStepNum">
        <nuxt-link to="/" class="btn-next btn btn-lg btn-primary">확인</nuxt-link>
      </template>
    </div>
    
  </section>
</template>

<script>
import step1 from '~/components/server/step1.vue'
import step2 from '~/components/server/step2.vue'
import step3 from '~/components/server/step3.vue'
import step4 from '~/components/server/step4.vue'
import step5 from '~/components/server/step5.vue'
import step6 from '~/components/server/step6.vue'

export default {
  components: {
    step1,
    step2,
    step3,
    step4,
    step5,
    step6
  },
  data () {
    return {
      stepNum: 5,
      maxStepNum: 6,
      selected: {
        serverImg: {
          bootingDiskSize: "53687091200",
          osType: 'os',
          osDetailType: 'ALL',
          dbmsOsDetailType: 'ALL'
        }
      },
      inputData: {
        serverImg: {
          name: null,
          description: null
        },
        server: {
          storageType: 'SSD',
          FeeSystemType: 'FXSUM',
          serverNum: 1,
          serverName: '',
          returnProtection: 'TRUE'
        },
        authentication: {
          authentication: 'sel',
          name: ''
        },
        setUpAcg: {
          type: 'new',
          name: ''
        }
      }
    }
  },
  methods: {
    goNext() {
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
