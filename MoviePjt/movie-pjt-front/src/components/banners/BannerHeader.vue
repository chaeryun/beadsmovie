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
      <span v-if="isLogin == true" @click="logout">LogOut &nbsp;&nbsp;</span>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "BannerHeader",

  data() {
    return {};
  },

  computed: {
    ...mapState({ isLogin: (state) => state.user.isLogin }),
  },

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

span:hover {
  cursor: pointer;
}
</style>
