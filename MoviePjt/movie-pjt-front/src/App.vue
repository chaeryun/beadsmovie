<template>
  <v-app>
    <v-main class="detail">
      <banner-header />

      <router-view />
      <hr />
<<<<<<< HEAD
      <banner-footer />
=======
>>>>>>> c9fa444f638fd3159099e9af92b9797cacedd282
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
<<<<<<< HEAD

<style>
hr {
  border-color:darkslategrey;
}

</style>
=======
>>>>>>> c9fa444f638fd3159099e9af92b9797cacedd282
