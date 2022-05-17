<template>
  <div  class="card text-white" style="width: 18%; height: 485px; background-color: rgba(50, 60, 65, 0.9)">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body d-flex align-items-start flex-column">
      <p class="card-title fw-bold fs-6 mb-auto">{{ movie.title }}</p>
     
    </div>
  </div>
</template>


<script>
import MovieDetail from "@/components/movie/MovieDetail"
import carousel from "vue-owl-carousel"
export default {
  name: "MovieCard",
  data: function () {
    return {
      poster: null,

    }
  },
  props:{
    movie: Object,

  },

  components: {
    MovieDetail,
    carousel
  },
  methods: {
   
  },
  created: function () {
    this.poster = `https://www.themoviedb.org/t/p/w440_and_h660_face/${this.movie.poster_path}`
  }
}
</script>


<style>
@font-face {
  font-family: "NewWaltDisney";
  src: url(../../fonts/NewWaltDisney.ttf) format("truetype");
}
@font-face {
  font-family: 'NanumSquareLight';
  src: url(../../fonts/NanumSquareL.ttf) format('truetype');
}
@font-face {
  font-family: 'NanumSquare';
  src: url(../../fonts/NanumSquareR.ttf) format('truetype');

}
@font-face {
  font-family: 'NanumSquareBold';
  src: url(../../fonts/NanumSquareB.ttf) format('truetype');

}
@font-face {
  font-family: 'NanumSquareExtraBold';
  src: url(../../fonts/NanumSquareEB.ttf) format('truetype');

}

.text {
  text-align: center;
  justify-content: center;
  font-family:  "NanumSquareExtraBold";
}
.centered { display: table; margin-left: auto; margin-right: auto;}
  .float {float:left;}




</style>