import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    result: {}
  },
  mutations: {
    set_result (state, result) {
      state.result = result
    }
  }
})

export default store
