<template>
  <v-app>
    
      <banner-header />
      <v-main class="detail">
      <router-view />
      <hr />
      <banner-footer />
      </v-main>
    
  </v-app>
</template>

<script>
import BannerHeader from "./components/banners/BannerHeader.vue";
import BannerFooter from "./components/banners/BannerFooter.vue";

export default {
  name: "App",

  components: {
    BannerHeader,
    BannerFooter,
  },
};
</script>

<style>
hr {
  border-color:darkslategrey;
}

</style>
