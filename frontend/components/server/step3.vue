<template>
  <section>

    <div class="form-horizontal">
      <h4>인증키 설정</h4>
      <p class="mt-10 color-gray">보유하고 있는 인증키를 선택하거나 새로운 인증키를 생성하세요. 인증키는 관리자 비밀번호를 얻는데 사용합니다. (<span class="color-primary">·</span> 필수 입력 사항입니다.) </p>
      <hr class="mv-30" style="border-color: #000;">

      <section>
        <label class="md-check"><input type="radio" name="authentication" value="sel" v-model="inputData.authentication"> <i class="blue"></i>
          보유하고 있는 인증키 이용
        </label>
        <div class="form-group" v-if="inputData.authentication === 'sel'">
          <label for="username" class="col-sm-2 control-label">인증키 선택</label>
          <div class="col-sm-9 input-wrap">
            <dropdown>- select -</dropdown>
          </div>
        </div>
      </section>

      <section class="mt-10">
        <label class="md-check"><input type="radio" name="authentication" value="new" v-model="inputData.authentication"> <i class="blue"></i>
          새로운 인증키 생성
        </label>
        <div class="form-group" v-if="inputData.authentication === 'new'">
          <label for="username" class="col-sm-2 control-label">인증키 이름</label>
          <div class="col-sm-9 input-wrap">
            <input placeholder="최소 3글자, 최대 30자" v-model="inputData.name">
            <p class="color-gray-light mt-20">인증키 이름을 입력 후 <span class="color-gray-darker">[인증키 생성 및 저장]</span>를 클릭하여 인증키를 사용자 컴퓨터에 저장하세요.<br>
            인증키는 해당 서버의 <span class="color-gray-darker">관리자 비밀번호 확인</span>에 이용되니 <span class="color-gray-darker">안전한 곳에 저장</span>하시기 바랍니다</p>
          </div>
        </div>
      </section>

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
  }
}
</script>
