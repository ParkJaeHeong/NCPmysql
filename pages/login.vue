<template>
  <section id="login">
  
    <h2 class="text-center">로그인</h2>
    <div class="mt-30">

      <div class="input-wrap" :class="{error: loginResult === '401' || (isSubmit && !usernameOk)}">
        <input type="text" placeholder="아이디(메일)" name="username" maxlength="100" title="아이디(이메일) 입력" tabindex="1" v-model="username"/>
        <!-- <div class="error-msg"><span>{{(isSubmit&&!usernameOk)? '아이디(메일)를 확인해 주세요.' : '잘못된 아이디 또는 비밀번호를 입력하셨습니다.'}}</span></div> -->
      </div>

      <div class="input-wrap mt-10" :class="{error: loginResult || (isSubmit && !passwordOk)}">
        <input type="password" placeholder="비밀번호" name="password" title="비밀번호 입력" tabindex="2" v-model="password">
        <!-- <div class="error-msg"><span>{{emailErrorMessage}}</span></div> -->
      </div>
            
      <label v-cloak check class="mt-10">
        <input type="checkbox" title="아이디 저장" tabindex="3" v-model="isCheckedSaveId">
        아이디 저장<i></i>
      </label>
      <button type="button" @click="login" class="btn-login btn btn-lg btn-block btn-primary mt-10">로그인</button>

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
    login () {
      console.log('login!')
    }
  }
}
</script>

<style lang="less" scoped>
#login {
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
