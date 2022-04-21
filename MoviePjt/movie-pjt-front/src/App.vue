<template>
  <v-app>
    <v-main>
      <sns-header />
      <hr />
      <router-view />
      <hr />
      <sns-footer />
    </v-main>
  </v-app>
</template>

<script>
import SnsHeader from "./components/sns/SnsHeader.vue";
import SnsFooter from "./components/sns/SnsFooter.vue";

export default {
  name: "App",

  components: {
    SnsHeader,
    SnsFooter,
  },
};
</script>

<style scoped>
hr {
  width: 75%;
  margin: 0px auto;
}
</style>
