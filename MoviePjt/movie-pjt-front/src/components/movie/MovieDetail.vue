<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="400" elevation="10">
          <v-img
            height="510px"
            width="410px"
            :src="this.generalurl + this.moviedetail.poster_path"
          >
          </v-img>
        </v-card>
      </v-col>

      <v-col cols="8" >
        <v-card flat style="background:rgba(0,0,0,0);">
          <v-card-title class="mt-10 pt-10 mb-3">
            <h1 class="mr-2" style="color: white;">{{ this.moviedetail.title }}</h1>
            <h3 style="color: slategrey; background:rgba(0,0,0,0);">{{ this.moviedetail.original_title }}</h3>
            <div style="background:rgba(0,0,0,0); " class="col-2" :key="i" v-for="(genre, i) in genrelist"></div>
          </v-card-title>
              <v-card-subtitle>
               <v-row >
    <v-col 
      cols="12"
      sm="10"
      md="8"
    >
    
      <v-sheet style="background:rgba(0,0,0,0);"
      >
        <v-chip-group
          multiple
          active-class="success--text"
        >
          <v-chip
            v-for="genre in genrelist"
            :key="genre"
          >
            {{ genre.name }}
          </v-chip>
        </v-chip-group>
      </v-sheet>
    </v-col>
  </v-row>
                
              </v-card-subtitle>
          <h3 class="ml-4 mb-2" style="color: white;">개봉일 : {{ this.moviedetail.release_date }}</h3>

          <h3 class="ml-4 mb-2 mt-7" style="color: white;">
            줄거리 : <br />{{ this.moviedetail.overview }}
          </h3>
        </v-card>
      </v-col>
      <v-col class="mb-2 mt-10">
        <div class="ml-10 pl-10" style="color: white;"><h1>예고편</h1></div>
        <br />
        <div class="video-container ml-10 pl-10">
          <iframe
            class="video-iframe"
            width="90%"
            height="400"
            :src="this.videourl +  this.moviedetail.youtube_path"
            frameborder="0"
            allowfullscreen
          ></iframe>
        </div>
      </v-col>
      <v-col cols="7">
        <div><h1 class="mt-10 ml-10" style="color: white;">영화 추천</h1></div>
        <div style="display: flex">
          <div>
            <v-img
              class="white--text align-end ml-10 mt-8"
              height="350px"
              width="250px"
              style="border-radius: 30px"
              src="https://www.themoviedb.org/t/p/w220_and_h330_face/6zBWSuYW3Ps1nTfeMS8siS4KUaA.jpg"
            >
            </v-img>
            <h3 class="text-center mt-5 ml-8" style="color: white;">리버 데일</h3>
          </div>
          <div>
            <v-img
              class="white--text align-end ml-10 mt-8"
              height="350px"
              width="250px"
              style="border-radius: 30px"
              src="https://www.themoviedb.org/t/p/w220_and_h330_face/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg"
            >
            </v-img>
            <h3 class="text-center mt-5 ml-8" style="color: white;">루프 라페타</h3>
          </div>
          <div>
            <v-img
              class="white--text align-end ml-10 mt-8"
              height="350px"
              width="250px"
              style="border-radius: 30px"
              src="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/rqeYMLryjcawh2JeRpCVUDXYM5b.jpg"
            >
            </v-img>
            <h3 class="text-center mt-5 ml-8" style="color: white;">워킹 데드</h3>
          </div>
        </div>
      </v-col>
    </v-row>
    
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "MovieDetail",

  data() {
    return {
      movieid: "",
      moviedetail: [],
      genrelist: [],
      generalurl: "https://www.themoviedb.org/t/p/w220_and_h330_face",
      videourl: "https://www.youtube-nocookie.com/embed/",
    };
  },

  created() {
    // movie id 값 가져오기
    this.movieid = this.$route.query._id;
    this.getMovieDetail();
  },

  methods: {
    async getMovieDetail() {
      await http({
        method: "GET",
        url: "/movie/" + this.movieid,
      })
        .then((res) => {
          console.log("moviedetail :", res);
          this.moviedetail = res.data;
          this.genrelist = res.data.genres;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>


<style>
/* @import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap"); */
/* @font-face {
  font-family: "NewWaltDisney";
  src: url(../../fonts/NewWaltDisney.ttf) format("truetype");
}
@font-face {
  font-family: "NanumSquareLight";
  src: url(../../fonts/NanumSquareL.ttf) format("truetype");
}
@font-face {
  font-family: "NanumSquare";
  src: url(../../fonts/NanumSquareR.ttf) format("truetype");
}
@font-face {
  font-family: "NanumSquareBold";
  src: url(../../fonts/NanumSquareB.ttf) format("truetype");
}
@font-face {
  font-family: "NanumSquareExtraBold";
  src: url(../../fonts/NanumSquareEB.ttf) format("truetype");
} */

h1 {
  font-family: "NanumSquareExtraBold";
}

h3 {
  font-family: "NanumSquare";
}

.detail {
  background-image: url('@/assets/background.png');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
