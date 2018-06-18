<template>
  <section id="join">

    <div class="container">
      <header class="text-center pv-md">
        <h2>회원가입</h2>
        <p class="mt-10 color-gray-light">쉽고 간편한 클라우드 서비스를 만나보세요</p>
      </header>

      <div class="row form-horizontal">
        <!-- 이용약관 동의 -->
        <div class="col-sm-8 col-sm-push-2 col-md-6 col-md-push-3" v-if="stepNum === 1">
          <h5>서비스 이용약관 <span class="color-primary">(필수)</span>
            <label check class="circle-chx pull-right">
              <input type="checkbox" name="chk" v-model="isCheckedService"><i></i>
            </label>
          </h5>
          <policyService class="policy-box"/> 
          
          <h5 class="mt-30">개인정보 수집 및 이용에 대한 안내 <span class="color-primary">(필수)</span>
            <label check class="circle-chx pull-right">
              <input type="checkbox" name="chk" v-model="isCheckedPrivacy"><i></i>
            </label>
          </h5>
          <policyPrivacy class="policy-box"/>

          <h5 class="mt-30">광고성 정보 수신 <span class="color-gray">(선택)</span>
            <label check class="circle-chx pull-right">
              <input type="checkbox" name="chk" v-model="isCheckedAd"><i></i>
            </label>
          </h5>
        </div>

        <div class="col-sm-10 col-sm-push-1 col-md-8 col-md-push-2">
          <!-- 회원정보 입력 -->
          <template v-if="stepNum === 2">
            <h5>1. 로그인 정보</h5>
            <hr class="mv-30" style="border-color: #000;">

            <div class="form-group">
              <label for="username" class="col-sm-3 control-label">아이디 <span class="small color-primary">(필수)</span></label>
              <div class="col-sm-9">
                <input type="email" class="form-control" placeholder="이메일을 입력해 주세요" name="username" tabindex="1" v-model="username"/>
              </div>
            </div>
            
            <div class="form-group">
              <label for="password" class="col-sm-3 control-label">비밀번호 <span class="small color-primary">(필수)</span></label>
              <div class="col-sm-9">
                <input type="password" class="form-control" placeholder="비밀번호를 입력해 주세요" name="password" tabindex="2" v-model="password">
              </div>
            </div>
            
            <div class="form-group">
              <label for="password2" class="col-sm-3 control-label">비밀번호 확인 <span class="small color-primary">(필수)</span></label>
              <div class="col-sm-9">
                <input type="password" class="form-control" placeholder="비밀번호를 한번 더 입력해 주세요" name="password2" tabindex="3">
                <p class="small color-gray-light mt-5">비밀번호는 8자 이상, 16자 이하의 영문자, 숫자 및 특수문자를 조합하여 사용해야 합니다</p>
              </div>
            </div>

            <hr class="mv-30">

            <h5 class="mt-40">2. 개인 정보</h5>
            <hr class="mv-20" style="border-color: #000;">

            <div class="form-group">
              <label for="username" class="col-sm-3 control-label">이름 <span class="small color-primary">(필수)</span></label>
              <div class="col-sm-9">
                <input type="text" class="form-control" placeholder="이름을 입력해 주세요" name="username" tabindex="4" v-model="fullname"/>
              </div>
            </div>

            <div class="form-group">
              <label for="username" class="col-sm-3 control-label">휴대폰 번호 <span class="small color-primary">(필수)</span></label>
              <div class="col-sm-9">
                <input type="text" class="form-control" placeholder="휴대폰 번호를 '-' 없이 입력해주세요" name="username" tabindex="5" v-model="mobile"/>
              </div>
            </div>

            <hr class="mv-30">
          </template>

          <template v-if="stepNum === 3">
            <h5>가입이 완료되었습니다</h5>
            <hr class="mv-20" style="border-color: #000;">

            <dl class="dl-join dl-horizontal mv-0">
              <dt>아이디</dt>
              <dd>{{username}}</dd>
              <dt>이름</dt>
              <dd>{{fullname}}</dd>
              <dt>휴대폰 번호</dt>
              <dd>{{mobile}}</dd>
            </dl>

            <hr class="mv-20">
          </template>

          <div class="text-center mt-40">
            <template v-if="stepNum !== 3">
              <button type="button" class="btn-prev btn btn-lg btn-default" @click="stepNum--" v-if="stepNum !== 1">이전</button>
              <button type="button" class="btn-next btn btn-lg btn-primary" @click="stepNum++">다음</button>
            </template>
            <template v-else>
              <nuxt-link to="/" class="btn-next btn btn-lg btn-primary">확인</nuxt-link>
            </template>
          </div>

        </div>
      </div>
    </div>
    
  </section>
</template>

<script>
import axios from '~/plugins/axios'
import policyService from '~/components/policy/service.vue'
import policyPrivacy from '~/components/policy/privacy.vue'

export default {
  components: {
    policyService,
    policyPrivacy
  },
  async asyncData () {
    let { data } = await axios.get('/api/users')
    return { users: data }
  },
  data () {
    return {
      stepNum: 1,
      isCheckedService: false,
      isCheckedPrivacy: false,
      isCheckedAd: false,
      username: '',
      password: '',
      fullname: '',
      mobile: '',
      joinResult: null,
      isSubmit: false,
      isCheckedSaveId: false
    }
  },
  methods: {
    join () {
      console.log('join!')
    }
  }
}
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";

  #join {
    .policy-box {
      width: 100%;
      height: 150px;
      overflow-x: hidden;
      font-size: 12px;
      padding: 15px;
      letter-spacing: -.36px;
      line-height: 1.5;
      border: 1px solid #dadada;
      background: #f6f7f8;
      word-wrap: break-word;
      white-space: pre-wrap;
      word-break:break-all;
    }

    .dl-join {
      dt, dd {
        line-height: 1.9;
      }
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
  }
</style>
