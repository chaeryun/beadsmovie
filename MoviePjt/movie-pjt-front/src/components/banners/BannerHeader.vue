<template>

    <div class="header">

        <img src="@/assets/logo.png" style="width:400px; margin-top: -70px;" />
        <div class="header-summary">
          <span
            ><router-link :to="{ name: 'home' }"
              >Home&nbsp;&nbsp;</router-link
            ></span
          >
          <span
            ><router-link :to="{ name: 'AllMovieListView' }">Movies </router-link>
            &nbsp;&nbsp;</span
          >
          <span
            ><router-link :to="{ name: 'ArticleList' }">Reviews </router-link>
            &nbsp;&nbsp;</span
          >
          <span v-if="isLogin == false"
            ><router-link :to="{ name: 'AccountView' }">Login</router-link>
          </span>

          <span v-if="isLogin == true"
            ><router-link :to="{ name: 'AccountMypage' }">MyPage</router-link>
            &nbsp;&nbsp;</span
          >
          <span class="logoutheader" v-if="isLogin == true" @click="logout"
            >LogOut &nbsp;&nbsp;</span
          >
        </div>

    </div>

</template>

<script>

import { mapState, mapMutations } from "vuex";
import http from "@/util/http-common";

export default {
  name: "BannerHeader",
  components: {

  },

  data() {
    return {
    
    };
  },

  created() {
 
  },

  computed: {
    ...mapState({ isLogin: (state) => state.user.isLogin }),
  },

  methods: {
    ...mapMutations("user", ["SET_USER_STATE"]),
    // logout
    logout() {
      this.SET_USER_STATE(false);
      localStorage.clear();
      alert("logout");
      this.$router.push({ name: "home" }).catch((err) => err);
    },

    // 전체 MovieList 가져오기
    ///async getMovieList() {
    ///  await http({
    ///    method: "GET",
    ///    url: "/movie/",
    ///  })
    ///    .then((res) => {
    ///      console.log("movielist :", res);
    ///      this.movielist = res.data;
    ///    })
    ///    .catch((err) => {
    ///      console.log(err);
    ///    });
    ///},

    //genre 가져오기
   

    // 검색기능
   
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");

@font-face {
  font-family: "NewWaltDisney";
  src: url(../../fonts/NewWaltDisney.ttf) format("woff");
}

.text-white {
  color: white !important;
}

.header {
  color: white;
  background-color:rgba(17, 53, 53, 100%);
  text-align: center;
  margin-top: 0px;
  font-size: 2.5rem;
  margin-bottom: -15px;
  height:160px;
}
.main-title {
  font-family: "Amatic SC", cursive;
}
.header-summary {
  margin-top: -100px;
  font-size: 2.5rem;
  font-family: "NewWaltDisney";
}

a {
  color: white;
  text-decoration: none;
}

.v-application a {
  color: white;
}

span:hover {
  cursor: pointer;
}

.v-input {
  max-width: 15%;
}


.logoutheader {
  color: white;
}
</style>
