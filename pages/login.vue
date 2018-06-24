<template>
  <section id="login">
  
    <h2 class="text-center">로그인</h2>
    <div class="mt-30">

      <div class="input-wrap">
        <input type="text" name="username" placeholder="아이디(메일)" :class="{ 'err': errors.has('username') }" title="아이디(이메일) 입력" tabindex="1" v-model="username" v-validate="'required|email'"/>
         <p class="font-sm color-danger mt-5" v-if="errors.has('username')">아이디(메일)를 확인해 주세요</p>
      </div>

      <div class="input-wrap mt-10">
        <input type="password" placeholder="비밀번호" name="password" :class="{ 'err': errors.has('password') }"  tabindex="2" v-model="password" v-validate="'required'">
      </div>
            
      <label v-cloak check class="mt-10">
        <input type="checkbox" title="아이디 저장" tabindex="3" v-model="isCheckedSaveId">
        아이디 저장<i></i>
      </label>
      <button type="button" @click="validateBeforeSubmit(login)" class="btn-login btn btn-lg btn-block btn-primary mt-10">로그인</button>

      <div class="mt-20 text-center">
        <nuxt-link :to="{ name: 'join' }" class="btn-join">회원가입</nuxt-link>
      </div>
    </div>
    
  </section>
</template>

<script>
export default {
  layout: 'panel',
  data () {
    return {
      username: '',
      password: '',
      loginResult: null,
      isSubmit: false,
      isCheckedSaveId: false
    }
  },
  methods: {
    validateBeforeSubmit (func) {
      this.$validator.validateAll().then((result) => {
        if (result) {
          // success process
          func()
        }
        // fail process
      })
    },
    login () {
      console.log('login!')
    }
  }
}
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";

  #login {
  input.err {
    border: 1px solid @brand-danger;
  }

  .btn-login {
    font-size: 14px;
  }

  .btn-join {
    color: #999;
    &:hover {
      color: #555;
    }
  }
}
</style>
