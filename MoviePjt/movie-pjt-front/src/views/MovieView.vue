<template>
<div class="background">
  <movie-main />
</div>
</template>

<script>
import MovieMain from "../components/movie/MovieMain.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",

  components: {
    MovieMain,
  },
};
</script>
<style>
.background {
  height:100vh;
  width: 100vw;
  overflow: scroll;
  background-attachment: local;
  background-image: url('@/assets/background.png');
  background-size:cover;
}

</style>
