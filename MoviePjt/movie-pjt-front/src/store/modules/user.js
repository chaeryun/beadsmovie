const user = {
  namespaced: true,

  state: {
    // login 상태여부
    isLogin: false,
    userInfo: [],
  },
  getters: {},
  mutations: {
    SET_USER_STATE(state, data) {
      state.isLogin = data;
    },
  },
  actions: {},
};

export default user;
