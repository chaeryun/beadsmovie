<template>
  <div class="header">
    <div>
      <h1 class="main-title">
        <router-link :to="{ name: 'home' }"
          >Beads Movie&nbsp;&nbsp;</router-link
        >
      </h1>
    </div>

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

      <span v-if="isLogin == true">MyPage &nbsp;&nbsp;</span>
<<<<<<< HEAD
      <span v-if="isLogin == true">LogOut &nbsp;&nbsp;</span>
=======
      <span v-if="isLogin == true" @click="logout">LogOut &nbsp;&nbsp;</span>
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
import { mapState } from "vuex";
=======
import { mapState, mapMutations } from "vuex";
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab

export default {
  name: "BannerHeader",

  data() {
    return {};
  },

  computed: {
    ...mapState({ isLogin: (state) => state.user.isLogin }),
  },

<<<<<<< HEAD
  methods: {},
=======
  methods: {
    ...mapMutations("user", ["SET_USER_STATE"]),
    // logout
    logout() {
      this.SET_USER_STATE(false);
      sessionStorage.clear();
      alert("logout");
      this.$router.push({ name: "home" }).catch((err) => err);
    },
  },
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");

.header {
  text-align: center;
  margin-top: 4.7rem;
  font-size: 2.5rem;
  margin-top: 2.7rem;
  margin-bottom: 2rem;
}
.main-title {
  font-family: "Amatic SC", cursive;
}
.header-summary {
  margin-top: 1rem;
  font-size: 2.5rem;
  font-family: "Amatic SC", cursive;
}

a {
  color: black;
  text-decoration: none;
}

.v-application a {
  color: black;
}
<<<<<<< HEAD
=======

span:hover {
  cursor: pointer;
}
>>>>>>> f1a715ec92d9e15bffc482c9c6d9feffdf2244ab
</style>
