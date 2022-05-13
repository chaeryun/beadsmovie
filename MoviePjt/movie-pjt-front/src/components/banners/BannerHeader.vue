<template>
  <div id="app">
    <sliding-header :threshold-hide="5000" :threshold-open="400">
      <template v-slot:header>
        <img width="380" src="@/assets/logo.png" />
        <div class="header-summary">
          <span
            ><router-link :to="{ name: 'home' }"
              >Movie&nbsp;&nbsp;</router-link
            ></span
          >
          <span
            ><router-link :to="{ name: 'ArticleList' }">Article </router-link>
            &nbsp;&nbsp;</span
          >
          <span>Interest &nbsp;&nbsp;</span>
          <span>Subscribe &nbsp;&nbsp;</span>
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

        <v-row>
          <v-col cols="10" align="right" color="white">
            <v-text-field
              color="white"
              style="max-width: 200px; margin-top: 20px"
              dark
              class="text-white"
              label="Search"
              prepend-icon="mdi-magnify"
              v-model="keyword"
              @keyup.enter="searchmovie(keyword)"
            ></v-text-field>
          </v-col>
        </v-row>
      </template>
    </sliding-header>
  </div>
</template>

<script>
import SlidingHeader from "./SlidingHeader.vue";
import { mapState, mapMutations } from "vuex";
import http from "@/util/http-common";

export default {
  name: "BannerHeader",
  components: {
    SlidingHeader,
  },

  data() {
    return {
      movielist: [],

      // 검색
      keyword: "",
      keywordlist: [],
    };
  },

  created() {
    this.getMovieList();
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
    async getMovieList() {
      await http({
        method: "GET",
        url: "/movie/",
      })
        .then((res) => {
          console.log("movielist :", res);
          this.movielist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 검색기능
    searchmovie(keyword) {
      console.log("keyword", keyword);

      // keyword 초기화
      this.keywordlist = [];

      for (let i = 0; i < this.movielist.length; i++) {
        if (
          this.movielist[i].title.toLowerCase().includes(keyword.toLowerCase())
        ) {
          // console.log("키워드 일치");
          this.keywordlist.push(this.movielist[i]);
          // console.log("키워드 일치 와인리스트", this.keywordlist);
        }
      }

      console.log("검색리스트", this.keywordlist);
      this.$router
        .push({ name: "MoveDetail", query: { search: keyword } })
        .catch((err) => err);
    },
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
.sliding-header {
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.3s;
}
.sliding-header.header {
  background-color: rgba(17, 53, 53, 85%);
  height: 80px;
}
.sliding-header.hidden {
  top: -100px;
}
.header {
  text-align: center;
  top: 0;
  font-size: 2.5rem;

  margin-bottom: 2rem;
}
.main-title {
  font-family: "Amatic SC", cursive;
}
.header-summary {
  margin-top: 1rem;
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
#app {
  text-align: center;
  margin-top: 100px;
  font-size: 2.5rem;
  top: 0;
}
.image-box {
  margin: 0 auto;
}
.image-thumbnail {
  margin: -100px auto;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.logoutheader {
  color: white;
}
</style>
