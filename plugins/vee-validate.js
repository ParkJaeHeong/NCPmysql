import Vue from 'vue'
import VeeValidate, { Validator } from 'vee-validate'
import ko from 'vee-validate/dist/locale/ko'

const customKo = {
  custom: {
    phone: {
      required: '휴대폰 번호를 입력해주세요',
      numeric: '휴대폰 번호는 숫자로만 입력해주세요',
      regex: '휴대폰 번호는 01012345678 형식으로 \'-\' 없이 입력해주세요'
    },
    name: {
      required: '이름을 입력해주세요'
    },
    username: {
      required: '이름을 입력해주세요'
    },
    code: {
      required: '인증번호를 입력해주세요'
    },
    email: {
      required: '이메일을 입력해주세요',
      email: '이메일 형식에 맞춰서 입력해주세요'
    },
    password: {
      required: '비밀번호를 입력해주세요'
    },
    confirmPassword: {
      required: '비밀번호를 입력해주세요',
      confirmed: '두 비밀번호가 일치하지 않습니다'
    },
    pwNew: {
      required: '비밀번호를 입력해주세요'
    },
    agreeService: {
      required: '필수 동의 항목입니다'
    },
    agreePrivacy: {
      required: '필수 동의 항목입니다'
    },
    agreePolicy: {
      equired: '필수 동의 항목입니다'
    },
    'validate-phone': {
      required: '인증번호를 입력해주세요'
    },
    birthday: {
      required: '생년월일을 입력해주세요',
      date_format: '형식에 맞게 입력해주세요. (20180111)'
    },
    gender: {
      required: '성별을 선택해주세요'
    },
    title: {
      required: '제목을 입력하세요'
    },
    content: {
      required: '문의 내용을 입력하세요'
    },
    buyerName: {
      required: '이름을 입력하세요'
    },
    businessNumber: {
      required: '생년월일 또는 사업자번호를 입력하세요',
      numeric: '숫자를 입력하세요'
    },
    cardNumber: {
      required: '카드번호를 입력하세요',
      numeric: '숫자를 입력하세요'
    },
    expireMonth: {
      required: '유효기간 (월)을 입력하세요',
      numeric: '숫자를 입력하세요'
    },
    expireYear: {
      required: '유효기간 (연)을 입력하세요',
      numeric: '숫자를 입력하세요'
    },
    cardPassword: {
      required: '카드 비밀번호를 입력하세요',
      numeric: '숫자를 입력하세요'
    },
    businessName: {
      required: '업체명을 입력하세요'
    },
    supplyName: {
      required: '대표자(공급자)명을 입력하세요'
    },
    businessImage: {
      required: '업체사진을 업로드 하세요'
    }
  }
}

// ko의 원래 dic을 먼저 불러오고 그 다음에 custom을 merge 시켜야 컴포넌트에서 extend를 사용할 수 있다.
Validator.localize('ko', ko)
Validator.localize('ko', customKo)

Vue.use(VeeValidate, {
  locale: 'ko'
})
