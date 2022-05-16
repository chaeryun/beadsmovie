<template>
  <div class="regist">
    <h1 class="underline">글 정보</h1>
    <div class="regist_form">
      <label for="title">이미지</label>
      <figure class="item">
        <v-img :src="`http://127.0.0.1:8000` + article.image" />
      </figure>
      <label for="title">제목</label>
      <div class="view">{{ article.title }}</div>
      <label for="author">작성자</label>
      <div class="view">{{ article.userName }}</div>
      <label for="price">작성일</label>
      <div class="view">
        {{ article.created_at | yyyyMMdd }}
      </div>
      <label for="content">내용</label>
      <div class="view" v-html="article.content"></div>
      <div>
        <v-btn v-if="islikes" icon color="blue" @click="like">
          <v-icon>mdi-thumb-up</v-icon>
        </v-btn>
        <v-btn v-else icon color="blue" @click="like">
          <v-icon>mdi-thumb-up-outline</v-icon>
        </v-btn>
      </div>
      <div>{{ likesNum }} 개</div>

      <div align="center" justify="space-around" style="margin: 2.5rem">
        <v-btn
          depressed
          dark
          x-large
          color="success"
          @click="moveModifyArticle()"
          >글수정</v-btn
        >
        <v-btn depressed dark x-large color="success" @click="deleteArticle()"
          >글삭제</v-btn
        >
        <v-btn depressed dark x-large color="success" @click="listArticle()"
          >목록</v-btn
        >
      </div>
    </div>
    <article-comment />
  </div>
</template>

<script>
import http from "@/util/http-common";
import VueJwtDecode from "vue-jwt-decode";

import ArticleComment from "./ArticleComment.vue";

export default {
  name: "ArticleDetail",
  components: {
    ArticleComment,
  },
  data() {
    return {
      article: {},
      user: [],
      me: [],
      likes: "",
      likesNum: "",
    };
  },
  created() {
    http.get(`/articles/detail/${this.$route.params.id}/`).then(({ data }) => {
      this.article = data;
      this.likesNum = this.article.like_users.length;
    });
    this.getUser();
  },
  methods: {
    getToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    listArticle() {
      this.$router.push({ name: "ArticleList" });
    },
    moveModifyArticle() {
      if (this.user.username === this.article.userName) {
        this.$router.replace({
          name: "ArticleUpdate",
          params: { id: this.article.id },
        });
      } else {
        alert("수정 권한이 없습니다!");
      }
    },
    deleteArticle() {
      if (this.user.username === this.article.userName) {
        if (confirm("정말로 삭제하시겠습니까?")) {
          this.$router.replace({
            name: "ArticleDelete",
            params: { id: this.article.id },
          });
        }
      } else {
        alert("삭제 권한이 없습니다!");
      }
    },
    getUser() {
      const config = this.getToken();
      const hash = localStorage.getItem("jwt");
      // console.log(VueJwtDecode.decode(hash));
      const info = VueJwtDecode.decode(hash);
      http.post(`/accounts/myprofile/`, info, config).then(({ data }) => {
        this.user = data;
        if (this.user.like_articles.includes(this.article.id)) {
          this.likes = true;
        } else {
          this.likes = false;
        }
      });
    },
    like() {
      const config = this.getToken();
      const item = {
        id: this.article.id,
        user: this.user.id,
      };

      http
        .post(
          `/articles/like/${this.user.id}/${this.article.id}/`,
          item,
          config
        )
        .then(() => {
          this.getUser();
          this.check();
        });
    },
    check() {
      if (this.likes) {
        this.likesNum -= 1;
      } else {
        this.likesNum += 1;
      }
    },
  },
  computed: {
    islikes() {
      return this.likes;
    },
  },
  filters: {
    yyyyMMdd: function (value) {
      // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
      if (value == "") return "";

      // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
      let js_date = new Date(value);

      // 연도, 월, 일 추출
      let year = js_date.getFullYear();
      let month = js_date.getMonth() + 1;
      let day = js_date.getDate();

      // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
      if (month < 10) {
        month = "0" + month;
      }

      if (day < 10) {
        day = "0" + day;
      }

      // 최종 포맷
      return year + "-" + month + "-" + day;
    },
  },
};
</script>

<style scoped>
.regist {
  padding: 10px;
  width: 75%;
  margin: 0px auto;
}
.regist_form {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
.underline {
  display: inline-block;
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0) 70%,
    rgb(0, 255, 76) 30%
  );
  margin-bottom: 3rem;
}
input,
textarea,
.view {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  color: #787878;
  font-size: medium;
}
label {
  display: inline-block;
  width: 80px;
}
button,
.btn {
  width: 8%;

  padding: 14px 20px;
  margin: 3rem;
  border-radius: 4px;
  font-size: large;
  cursor: pointer;
  border-radius: 2rem;
  text-decoration-line: none;
}
.item {
  width: 30%;
}
</style>
