<template>
  <section>

    <div class="form-horizontal">
      <h4>네트워크 접근 설정</h4>
      <p class="mt-10 color-gray">보유하고 있는 ACG를 선택하거나 새로운 ACG를 생성해주세요.<br>
      <span class="color-primary">ACG(Access Control Group)은 별도의 방화벽 구축없이, 서버 그룹에 대한 네트워크 접근 제어 및 관리를 돕는 상품입니다.</span></p>
      <hr class="mv-30" style="border-color: #000;">

      <section>
        <label class="md-check"><input type="radio" name="setUpAcg" value="new" v-model="inputData.type"> <i class="blue"></i>
          신규 ACG 생성
        </label>
        <button type="button" class="btn btn-sm btn-primary ml-20" v-if="inputData.type === 'new'">+ ACG 생성</button>
      </section>

      <section class="mt-10">
        <label class="md-check"><input type="radio" name="setUpAcg" value="sel" v-model="inputData.type"> <i class="blue"></i>
          보유하고 있는 ACG 중에서 선택
        </label>
        <template v-if="inputData.type === 'sel'">
          <div class="form-group">
            <label for="username" class="col-sm-2 control-label">인증키 이름</label>
            <div class="col-sm-9 input-wrap">
              <multi-select v-model="selected" :options="options"/>
              <p class="color-gray mt-10">최대 5개까지 선택가능</p>
            </div>
          </div>
          <p>설정 시 주의사항</p>
          <ul class="mt-10">
            <li class="color-danger">복수로 ACG 선택 시 Shift를 이용해야 합니다.</li>
            <li class="color-danger">서버 생성 후에는 ACG를 변경하거나, 추가하는 것은 지원하지 않습니다.</li>
            <li>선택한 ACG의 세부 설정은 콘솔 내 'SERVER > ACG' 메뉴에서 가능합니다.</li>
          </ul>
        </template>
      </section>

    </div>
    <hr class="mt-30">

  </section>
</template>

<script>
import { Dropdown, MultiSelect } from 'uiv'

export default {
  components: {
    Dropdown,
    MultiSelect
  },
  props: {
    inputData: {
      type: Object
    },
    nextFunc: {
      type: Function
    }
  },
  data () {
    return {
      selected: [],
      options: [
        {value: 1, label:'Option1'},
        {value: 2, label:'Option2'},
        {value: 3, label:'Option3'},
        {value: 4, label:'Option4'},
        {value: 5, label:'Option5'}
      ]
    }
  }
}
</script>
