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
          <label class="col-sm-2 control-label">인증키 선택</label>
          <div class="col-sm-9 input-wrap">
            <dropdown ref="dropdown">
              <btn type="default" class="dropdown-toggle">{{ inputData.name }}<span class="caret ml-10"></span></btn>
              <template slot="dropdown">
                <li class="dropdown-item" v-for="title in inputData.list" @click="inputData.name = title"><a>{{title}}</a></li>
              </template>
            </dropdown>
          </div>
        </div>
      </section>

      <section class="mt-10">
        <label class="md-check"><input type="radio" name="authentication" value="new" v-model="inputData.authentication"> <i class="blue"></i>
          새로운 인증키 생성
        </label>
        <div class="form-group" v-if="inputData.authentication === 'new'">
          <label class="col-sm-2 control-label">인증키 이름</label>
          <div class="col-sm-8 input-wrap">
            <div class="input-group">
              <input type="text" class="form-control" placeholder="최소 3글자, 최대 30자" v-model="inputData.addName" v-validate="'required|min:3|max:30'">
              <span class="input-group-btn">
                <button type="button" class="btn btn-default" @click="addAuthentication(inputData.addName)" :disabled="inputData.addName === ''">인증키 생성 및 저장</button>
                <!--<btn type="default" @click="addAuthentication(inputData.addName)">인증키 생성 및 저장</btn>-->
              </span>
            </div>
            <p class="color-gray-light mt-20">인증키 이름을 입력 후 <span class="color-gray-darker">[인증키 생성 및 저장]</span>를 클릭하여 인증키를 사용자 컴퓨터에 저장하세요.<br>
              인증키는 해당 서버의 <span class="color-gray-darker">관리자 비밀번호 확인</span>에 이용되니 <span class="color-gray-darker">안전한 곳에 저장</span>하시기 바랍니다</p>
          </div>
        </div>
      </section>

    </div>
    <hr class="mv-40">

    <div class="text-center">
      <button type="button" class="btn-prev btn btn-lg btn-default" @click="prevFunc">이전</button>
      <button type="button" class="btn-next btn btn-lg btn-primary" @click="nextFunc" :disabled="inputData.name === '선택해주세요'">다음</button>
    </div>

  </section>
</template>

<script>
  import {Dropdown, Btn} from 'uiv'

  export default {
    components: {
      Dropdown,
      Btn
    },
    props: {
      inputData: {
        type: Object
      },
      nextFunc: {
        type: Function
      },
      prevFunc: {
        type: Function
      }
    },
    methods: {
      addAuthentication (name) {
        this.inputData.list.push(name)
        this.inputData.addName = ''
        this.inputData.authentication = 'sel'
        console.log(this.inputData.list)
      }
    }
  }
</script>
