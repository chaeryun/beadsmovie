<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="400" elevation="10">
          <v-img
            height="100%"
            width="100%"
            :src="this.generalurl + this.moviedetail.poster_path"
          >
          </v-img>
        </v-card>
      </v-col>

      <v-col cols="8">
        <v-card  flat style="background:rgba(0,0,0,0);">
          <v-card-title class="mt-10 pt-10 mb-3">
            <h1 class="mr-2" style="color: white;">{{ this.moviedetail.title }}</h1>
            <h3 style="color: slategrey; background:rgba(0,0,0,0);">{{ this.moviedetail.original_title }}</h3>
            <div style="background:rgba(0,0,0,0); " class="col-2" :key="i" v-for="(genre, i) in genrelist"></div>
          </v-card-title>
              <v-card-subtitle>
               <v-row>
    <v-col 
      cols="12"
      sm="10"
      md="8"
    >
    
      <v-sheet style="background:rgba(0,0,0,0);"
      >
        <v-chip-group
          multiple
          active-class="red--text"
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
        <v-col  style="color: white;"><h1>예고편</h1></v-col>
        <br />
        <div class="video-container">
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
<br/>
      <v-col>
        
        <v-col><h1 class="mt-10 mb-8" style="color: white;">영화 추천</h1></v-col>
 


        <v-row   justify="center" class="mb-8" >
          <v-col cols="4" v-for="movie in similar_movielist" :key="movie">
          
                  
                    <v-card
                    style="
                      z-index: 1;
                      height: 370px;
                      margin: auto;
                      border-radius: 10px;
                      background-color:darkslategrey;
                      box-shadow: 0 0 10px grey;
                    "
                    hover
                    outlined
                  >
                    <v-img 
                      :src="generalurl + movie.poster_path"
                      height="300"
                      style="margin-top: 10px; margin-bottom : 10px;"
                      contain
                      @click="gomoviedetail(movie._id)"
                    ></v-img>
                    
                    <hr class="recommend_line" />
                    <v-card-text
                      class="text-center"
                      style="color: white; font-size:medium;"
                      >{{ movie.title }}
                    </v-card-text>
                  </v-card>
                </v-col>
                  <img style="z-index:0; position:absolute;  width:240px; height:280px" src="@/assets/loading.gif">
              </v-row>
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
      recentlist: [],
      genrelist: [],
      similar_movielist: [],
      generalurl: "https://www.themoviedb.org/t/p/w220_and_h330_face",
      videourl: "https://www.youtube-nocookie.com/embed/",
    };
  },

  created() {
    // movie id 값 가져오기
    this.movieid = this.$route.query._id;
    this.getMovieDetail();
    this.getSimilarMovieDetail();
  },

  computed : {
    startOffset() {
      return (this.currentPage - 1) * this.perPage;
    },
    endOffset() {
      return this.startOffset + this.perPage;
    },
    numOfPages() {
      return Math.ceil(this.recentlist.length / this.perPage);
    },
    calData() {
      return this.recentlist.slice(this.startOffset, this.endOffset);
    },

    movielistIsEmpty() {
      // console.log(this.recentlist.length);
      return this.recentlist.length == 0;
    },
  },
  

  methods: {
    async getMovieDetail() {
      await http({
        method: "GET",
        url: "/movie/" + this.movieid,
      })
        .then((res) => {
          // console.log("moviedetail :", res);
          this.moviedetail = res.data;
          this.recentlist = this.moviedetail;
          this.genrelist = res.data.genres;
          this.templist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 추천영화 가져오기
     async getSimilarMovieDetail() {
      await http({
        method: "GET",
        url: "/similar_movie/" + this.movieid,
      })
        .then((res) => {
          // console.log("similar_movielist :", res);
          this.similar_movielist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 추천영화 상세페이지 이동
    gomoviedetail(movie_id) {
      this.$router
        .push({ path: "/moviedetail", query: { _id: movie_id } })
        .catch(() => {});
      location.reload();
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
  
  background-color: rgba(17, 53, 53, 100%);
  background-image: url('@/assets/background.png');
 
  
 
  
  background-size: 100vw, auto, contain;
}

.recommend_line{
  border-color:silver;
  border-width: 2px;
}

</style>
