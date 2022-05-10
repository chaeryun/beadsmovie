<template>
  <div>
    

            <div class="image-box" >
              <img src="@/assets/harrypotter.png" class="image-thumbnail" width="1550" >
            </div>

          <div class="image-box" >
              <img src="@/assets/harrypotter2.png" class="image-thumbnail" width="1550" >
            </div>
   
          <div class="image-box" >
              <img src="@/assets/harrypotter3.png" class="image-thumbnail" width="1550">
            </div>

    <!-- Top 10 Movies -->
  
    <v-card-title
      class="text-h2 fw-bold"
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: Amatic SC, cursive !important;
      "
    >
      Top 10 Movies
    </v-card-title>
    <MovieCard :movies="top_movies"/>

    <!-- Action -->
    <v-card-title
      class="text-h2 fw-bold"
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: Amatic SC, cursive !important;
      "
    >
      Action
    </v-card-title>
    <MovieCard :movies="action_movies"/>
    
    <!-- Animation -->
    <v-card-title
      class="text-h2 fw-bold"
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: Amatic SC, cursive !important;
      "
    >
      Animation
    </v-card-title>
    <MovieCard :movies="animation_movies"/>

    <!-- Comedy -->
    <v-card-title
      class="text-h2 fw-bold"
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: Amatic SC, cursive !important;
      "
    >
      Comedy
    </v-card-title>
    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/wFjboE0aFZNbVOF05fzrka9Fqyx.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>애덤 프로젝트</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/r97txZRmBb75SGsIAWqmplWJnO3.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메탈 로드</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/edYk5TSowZIDv138bCpF5ls3XI5.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>더 버블</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>루프 라페타</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    <!-- Romance -->
    <v-card-title
      class="text-h2 fw-bold"
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: Amatic SC, cursive !important;
      "
    >
      Romance
    </v-card-title>

    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/iABPzTM6r5gfvnSmD7z0LblW71s.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메리 미</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/thqgzBPEDYQX0taszVus5nYMtTZ.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>문 샷</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/vdgUNCruHI6jX9TU4vvplgpDtL7.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>배틀 : 프리스타일</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/9Xd459BvOLFfPPzNfAPT9dZkO1x.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>웨스트 사이드 스토리</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import MovieCard from "@/components/movie/MovieCard";



export default 
{
  name: "MovieMain",
  data: function () {
    return {
       options: {
          rewind : true,
          width  : 800,
          gap    : '1rem',
        },
      movies: [],
      movie: '',

    }
  },
  components: {
    MovieCard,
},

  methods: {
    detail() {
      this.$router.push({ name: "MoveDetail" });
    },
    getMovieDatas: function () {
      axios.get(`https://beadsmovie.com/api/movie/`)
      .then( 
        (res) => { console.log(res);
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data
        }
      
       
      })
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");


.mx-auto {
  margin-top: 2rem;
}

.main-font {
  font-family: "Amatic SC", cursive;
}
.image-box {
  margin: 0 auto;
}
.image-thumbnail {
  margin: -100px auto;
  width:100%;
  height:100%;
  object-fit:cover;
}
</style>
