<template>
  <div class="all">

     <div class="text-center">
       <br />
      
      <v-btn class="genre_button" @click="clickgenre($event)" value="28">
        액션
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="12">
        모험
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="16">
        애니메이션
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="35">
        코미디
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="80">
        범죄
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="99">
        다큐멘터리
      </v-btn>
     
      <v-btn class="genre_button" @click="clickgenre($event)" value="18">
        드라마
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="10751">
        가족
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="14">
        판타지
      </v-btn>
      <br/>
      <v-btn class="genre_button" @click="clickgenre($event)" value="36">
        역사
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="27">
        공포
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="10402">
        음악
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="9648">
        미스터리
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="10749">
        로맨스
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="878">
        SF
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="10770">
        TV영화
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="53">
        스릴러
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="10752">
        전쟁
      </v-btn>
      <v-btn class="genre_button" @click="clickgenre($event)" value="37">
        서부
      </v-btn>
      
      


      </div>
      <!-- <v-bottom-navigation
          color="white"
          width="300px"
          style="
            border-radius: 10px;
            background-color:cadetblue;
            text-align: center;
          "
        >
        <v-btn value="red" @click="typered">
          <span class="fs-1">최신 개봉일순</span>
        </v-btn>

        <v-btn value="white" @click="typewhite">
          <span class="fs-1">오래된 순</span>
        </v-btn>

        <v-btn value="rose" @click="typerose">
          <span class="fs-1">인기순</span>
        </v-btn>

      </v-bottom-navigation> -->

<template v-if="movielistIsEmpty">
        <div class="justify-center mt-15" style="display: flex">
          <img
            src="../assets/loading.gif"
            style="width: 300px; height: 300px"
            alt="empty"
          />
        </div>
      </template>
      <v-row   v-else>
        <div
          class="col-xl-3 col-lg-4 col-md-6"
          :key="i"
          v-for="(movie, i) in calData"
        >
          <v-card
            class="mx-auto mt-10"
            max-width="430"
            style="
              border-radius: 30px;
              height: 530px;
              color: gainsboro;
              background-color: darkslategrey;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
          <br />
            <v-img
              :src="generalurl + movie.poster_path"
              height="450"
              alt="No image"
              contain
              @click="gomoviedetail(movie._id)"
            /><v-img />
            <v-card-title class="justify-center"
              ><h3>{{ movie.title }}</h3></v-card-title
            >
            <div
              class="d-flex justify-content-between align-items-center"
            ></div>
          </v-card>
        </div>
      </v-row>
      <v-row>
        <v-col col="4"></v-col>
        <v-pagination
          v-model="currentPage"
          :length="numOfPages"
          :total-visible="10"
          style="margin-top: 10px; margin-bottom: 10px; align-items:center;"
        ></v-pagination>
        <v-col col="4"></v-col>
      </v-row>


    </div>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Movie",
  data: () => ({
    recentlist: [],
    allmovielist: [],
    recentmovielist: [],
    oldmovielist: [],
    popularmovielist: [],
    
    templist: [],
    generalurl: "https://www.themoviedb.org/t/p/w220_and_h330_face",

    //검색기능
    keyword: "",

    //검색영화리스트
    keywordlist: [],

    currentPage: 1,
    perPage: 20,

    gerne: "",
    genrelist: [],
    

  }),

  created() {
    // movie page 클릭시 함수호출
    this.getMovieList();
  },

  computed: {
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
    // 전체 영화 불러와서 movielist에 넣기
    async getMovieList() {
      await http({
        method: "get",
        url: "/movie/",
      })
        .then((res) => {
          // console.log("movie list :", res);
          this.movielist = res.data;
          this.recentlist = this.movielist;
          this.templist = res.data;

          // console.log("movielist", this.movielist);
          this.typemovie(res.data);
      

        })
        .catch((err) => {
          console.log(err);
        });
    },

  

    // 상세페이지 이동
    gomoviedetail(movie_id) {
      this.$router
        .push({ path: "/moviedetail", query: { _id: movie_id } })
        .catch(() => {});
      location.reload();
    },

    // genre button 클릭시 해당장르영화 가져오기
    clickgenre(e) {
      this.genre_id =
        e.target.value === undefined ? e.currentTarget.value : e.target.value;

      this.genreclick();
    },

    async genreclick() {
      await http({
        methods: "get",
        url: "movie/genre/" + this.genre_id + "/",
      })
        .then((res) => {
          // console.log(res);
          this.genrelist = res.data;
          this.recentlist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

  typemovie(movie) {
      // 배열초기화
      this.adventurelist = [];
      this.romancelist = [];
      this.animationlist = [];
      this.comedylist = [];
      this.actionlist = [];
      this.dramalist = [];
      this.familylist = [];
      this.fantasylist = [];
      this.historylist = [];
      this.horrorlist = [];
      this.musiclist = [];
      this.misterylist = [];
      this.sflist = [];
      this.tvlist = [];
      this.thrillerlist = [];
      this.warlist = [];
      this.westlist = [];

      for (let i = 0; i < movie.length; i++) {
        if (movie[i].genre_id == "12") {
          this.adventurelist.push(movie[i]);
        } else if (movie[i].genre_id == "16") {
          this.animationlist.push(movie[i]);
        } else if (movie[i].genre_id == "35") {
          this.comedylist.push(movie[i]);
        } else if (movie[i].genre_id == "10749") {
          this.romancelist.push(movie[i]);
        } else if (movie[i].genre_id == "80") {
          this.actionlist.push(movie[i]);
        } else if (movie[i].genre_id == "18") {
          this.dramalist.push(movie[i]);
        } else if (movie[i].genre_id == "10751") {
          this.familylist.push(movie[i]);
        } else if (movie[i].genre_id == "14") {
          this.fantasylist.push(movie[i]);
        } else if (movie[i].genre_id == "36") {
          this.historylist.push(movie[i]);
        } else if (movie[i].genre_id == "27") {
          this.horrorlist.push(movie[i]);
        } else if (movie[i].genre_id == "10402") {
          this.musiclist.push(movie[i]);
        } else if (movie[i].genre_id == "9648") {
          this.misterylist.push(movie[i]);
        } else if (movie[i].genre_id == "878") {
          this.sflist.push(movie[i]);
        } else if (movie[i].genre_id == "10770") {
          this.tvlist.push(movie[i]);
        } else if (movie[i].genre_id == "53") {
          this.thrillerlist.push(movie[i]);
        } else if (movie[i].genre_id == "10752") {
          this.warlist.push(movie[i]);
        } else if (movie[i].genre_id == "37") {
          this.westlist.push(movie[i]);
        }

      }
    },

}
}

</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");
@font-face {
  font-family: "NewWaltDisney";
  src: url(../fonts/NewWaltDisney.ttf) format("truetype");
}
@font-face {
  font-family: 'NanumSquareBold';
  src: url(../fonts/NanumSquareL.ttf) format('truetype');
}

.all{
  font-family: 'NanumSquareBold';
}

.genre_button{
  box-shadow: 0 0 10px #3b3b34;
  color: white !important;
  height: 50px !important;
  border-radius: 40px;
  margin: 12px;
  background-color: darkslategrey !important; 
  font-weight: bold !important; 
  font-size:large !important;
  padding: 20px !important;
}

</style>