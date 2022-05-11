<template>
  <div>



  <div class="image-box">
  <carousel :autoplay="true" :nav="false" :dots="true"  items="1" >

    <div><img src="@/assets/image0.png" > <h1>신동덤덤</h1></div>
    <img src="@/assets/image1.jpg"  >
    <img src="@/assets/image2.png"  >
    <img src="@/assets/image0.png" >

  </carousel>
  </div>
    

    <!-- Top 10 Movies -->
  
    <v-card-title
      style="
        margin-left: 190px;
        margin-top: 50px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Top 10 Movies
    </v-card-title>
    <MovieCard :movies="top_movies"/>
    <v-container style="display: flex">
      <v-card

        max-width="100%"
        elevation="10"
        min-width="370px"
        min-height="350px"
        style="background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0)), url(https://www.themoviedb.org/t/p/w220_and_h330_face/qcOFxYpBvU8LwaMyKdjCoP7y7we.jpg) center center ;"

      >


        <v-card-subtitle >
          <h2 style="color:#fff" >배신의 만찬</h2>
          <h2></h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text @click="detail"> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      </v-container>
     
    <!-- Action -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Action
    </v-card-title>
    <MovieCard :movies="action_movies"/>
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
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/bCz71ysciwNL2xddSm25ufrgZ7V.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>더 배트맨</h2>
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
          src="https://mblogthumb-phinf.pstatic.net/MjAyMDEwMDJfMTE4/MDAxNjAxNjA5OTI1MDkx.iGd-vZulv298Brk8HAmipq10gf0OjKULrFpaqfagCh0g.02yjTFQ0NaVI3Wztsn6nKxGU5ePYKrNmnA0K3E2B_lsg.JPEG.cubase777/MV5BMDk5Yzc4NzMtODUwOS00NTdhLTg2MjEtZTkzZjc0ZWE2MzAwXkEyXkFqcGdeQXVyMTA3MTA4.jpg?type=w800"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>수퍼 소닉 (2020)</h2>
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
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/voddFVdjUoAtfoZZp2RUmuZILDI.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>스파이더맨 : 노 웨이 홈</h2>
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
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/nOYyuJ2mNo6RWsFsTwApEyG3F4J.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>야차</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    
    <!-- Animation -->
    <v-card-title

      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Animation
    </v-card-title>
    <MovieCard :movies="animation_movies"/>
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
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3eElpVmCeMqplQbkQd0y1fftL04FkfbQZrjKbEuhg3D6rQuKf"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>아이스 에이지: 벅의 대모험 (2022)</h2>
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
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/78JfwRiubwX87BYgPXsdFKBf9P5.jpg"
        >
        </v-img>
        <v-card-subtitle class="pb-0">
          <h2>pil</h2>
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
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/hsOhOcX7qDy7bPwbrt1OoITngrf.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메이의 새빨간 비밀</h2>
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
          src="https://blog.kakaocdn.net/dn/II2OM/btrpoVuvWts/b9rK1lvjxUFVox60anaKmK/img.png"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>엔칸토: 마법의 세계 (2021)</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>


    <!-- Comedy -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
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
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
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
import carousel from 'vue-owl-carousel'

export default 
{
  name: "MovieMain",

  data: function () {
    return {
      movies: [],
      movie: '',

    }
  },
   
  components: {
    MovieCard,
    carousel,
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
        }
      )},
   
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");
@font-face {
  font-family: "NewWaltDisney";
  src: url(../../fonts/NewWaltDisney.ttf) format('woff');
};


.mx-auto {
  margin-top: 2rem;
  
}

.main-font {
  font-family: "Amatic SC";
}
.image-box {
  margin: -25px auto;
}
.image-thumbnail {

  margin: -100px auto;
  width:100%;
  height:100%;
  object-fit:cover;



}
.title {
  display: flex;

  align-items: flex-end;
}
</style>
