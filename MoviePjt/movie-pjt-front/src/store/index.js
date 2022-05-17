import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import user from "./modules/user.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
  },
/*
  plugins: [createPersistedState()],
  state: {
    movieCards: [],
    popular: [],
    
  },
  mutations: {
    SET_POPULAR(state, data){
      state.popular = data;
    },
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    }
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/movie/',
      })
      .then((res) => {
        console.log(res)
        commit('LOAD_MOVIE_CARDS', res.data.results)
      })

    }
  },
  */
});
