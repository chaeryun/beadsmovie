const user = {
<<<<<<< HEAD
  state: {
    namespaced: true,

=======
  namespaced: true,

  state: {
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab
    // login 상태여부
    isLogin: false,
    userInfo: [],
  },
  getters: {},
<<<<<<< HEAD
  mutations: {},
=======
  mutations: {
    SET_USER_STATE(state, data) {
      state.isLogin = data;
    },
  },
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab
  actions: {},
};

export default user;
