<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="400" elevation="10">
          <v-img
            height="500px"
            width="400px"
            :src="this.generalurl + this.moviedetail.poster_path"
          >
          </v-img>
        </v-card>
      </v-col>

      <v-col cols="8">
        <v-card flat>
          <v-card-title class="mt-10 pt-10 mb-3">
            <h1>{{ this.moviedetail.title }}</h1>
          </v-card-title>
          <v-card-subtitle>액션 / 스릴러 </v-card-subtitle>
          <h3 class="ml-4 mb-2 mt-5">Original title : All the Old Knives</h3>
          <h3 class="ml-4 mb-2">TMDB Popularity : 3421.136</h3>
          <h3 class="ml-4 mb-2">TMDB Vote Average: ★★★☆☆</h3>
          <h3 class="ml-4 mb-2">Release date : 2022.04.08</h3>

          <h3 class="ml-4 mb-2 mt-3">
            Overview : <br />CIA 요원이자 전 연인(크리스 파인, 탠디 뉴턴)이 구출
            임무를 실패하고 몇 년이 지난 뒤 재회하고, <br />
            업무와 개인적인 감정을 구분하지 못한다. 국제 스파이 행위, 도덕적
            딜레마, <br />
            그리고 치명적인 배신을 다룬 눈을 뗄 수 없는 이야기다.
          </h3>
        </v-card>
      </v-col>
      <v-col class="mb-2 mt-10">
        <div class="ml-10 pl-10"><h1>Trailer</h1></div>
        <br />
        <div class="video-container ml-10 pl-10">
          <iframe
            class="video-iframe"
            width="90%"
            height="400"
            :src="`https://www.youtube-nocookie.com/embed/DfQx5kfERwE`"
            frameborder="0"
            allowfullscreen
          ></iframe>
        </div>
      </v-col>
      <v-col cols="7">
        <div><h1 class="mt-10">Movie Recommend</h1></div>
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
            <h3 class="text-center mt-5">리버 데일</h3>
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
            <h3 class="text-center mt-5">루프 라페타</h3>
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
            <h3 class="text-center mt-5">워킹 데드</h3>
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
      generalurl: "https://www.themoviedb.org/t/p/w220_and_h330_face",
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

.detail_page {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
