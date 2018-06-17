<template>
  <header class="container-fluid clearfix">
    <h1 class="pt-20 pull-left"><nuxt-link :to="'/'">NAVER CLOUD PLATFORM</nuxt-link></h1>
    <ul class="list-menu list-unstyled list-inline pull-right pt-20">
      <li><nuxt-link :to="{ name: 'login' }" class="btn btn-sm btn-primary">로그인</nuxt-link></li>
      <li><nuxt-link :to="{ name: 'join' }" class="btn btn-sm btn-default">회원가입</nuxt-link></li>
    </ul>
  </header>
</template>

<style lang="less" scoped>
  header {
    background-color: #fff;
    border-bottom: 1px solid #f5f5f5;

    h1 {
      padding-bottom: 10px;
      
      > a {
        display: block;
        width: 200px;
        height: floor((68/404)*200px);
        font-size: 0;
        background: url('/img/logo.png') 0 0 no-repeat/contain;
      }
    }
  }
</style>
