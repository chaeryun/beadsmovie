<template>
  <div>
    <v-container style="display: flex; justify-content: space-between; ">
    <carousel :autoplay="false" :nav="false" :dots="false"  :items="3"  >
    <div v-for="card in movieCard"
    :key="card.id">
      <v-card
      
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px;"
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="imgUrl"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>{{ card.title }}</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>
      </div>
    </carousel>
    </v-container>
    
    
  </div>
</template>

<script>
import MovieDetail from "@/components/movie/MovieDetail"
import carousel from "vue-owl-carousel"
export default {
  name: "MovieCard",
  data: function () {
    return {

    }
  },
  props: ['movieCard'],
  components: {
    MovieDetail,
    carousel
  },
  methods: {
   
  },
  computed: {
    imgUrl: function () {
      return `https://image.tmdb.org/t/p/w200/${this.card.poster_path}`
    }
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



</style>