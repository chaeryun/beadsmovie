<template>
  <v-app>
    <v-main class="detail">
      <banner-header />

      <router-view />
      <hr />
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
