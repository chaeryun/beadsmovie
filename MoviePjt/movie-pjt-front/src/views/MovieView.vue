<template>
  <movie-main />
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
  max-width: 50px;
  max-height: 100px;
  
  
  
  background-attachment: local;
  background-image: url('@/assets/background.png') ;
  background-size:cover;
}

</style>
