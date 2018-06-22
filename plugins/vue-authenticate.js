import Vue from 'vue'
import VueAxios from 'vue-axios'
import VueAuthenticate from 'vue-authenticate'
import axios from 'axios'

let options = {
  baseUrl: process.env.API_SERVER_ADDRESS,
  tokenName: 'access_token',
  tokenPrefix: 'qs_p',
  // tokenHeader: 'Authorization',
  // tokenType: 'Bearer',
  loginUrl: '/api/auth/login',
  registerUrl: '/api/signup',
  // logoutUrl: null,
  storageType: 'cookieStorage',
  // storageNamespace: 'vue-authenticate',
  cookieStorage: {
    domain: window.location.hostname,
    path: '/',
    secure: process.env.NODE_ENV === 'production'
  }
}

axios.defaults.baseURL = process.env.API_SERVER_ADDRESS

Vue.use(VueAxios, axios)
Vue.use(VueAuthenticate, options)
