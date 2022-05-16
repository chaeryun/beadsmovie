<template>
  <v-container class="container">
    <hr />
    <div>
      <v-row>
        <div class="commentform">
          <div>댓글 작성</div>
          <v-textarea
            v-model.trim="comment_content"
            auto-grow
            outlined
            rows="4"
            row-height="40"
            row-width="100"
            label="글 내용"
            placeholder="내용 입력..."
            required="required"
            prepend-icon="mdi-comment"
          ></v-textarea>
        </div>
        <v-btn
          class="commentbtn"
          @click="commentCreate"
          type="submit"
          color="success"
          depressed
          x-large
        >
          댓글 작성
        </v-btn>
      </v-row>
    </div>
    <v-card class="card-comment">
      <v-list two-line>
        <template v-for="(comment, index) in comments.slice(0, 6)">
          <v-divider :key="index"></v-divider>
          <v-list-item :key="comment.content">
            <v-list-item-avatar>
              <img
                src="https://cdn.pixabay.com/photo/2016/12/31/21/22/discus-fish-1943755_1280.jpg"
              />
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="comment.userName"></v-list-item-title>
              <v-list-item-content
                v-html="comment.content"
                style="font-size: 3rem"
              ></v-list-item-content>
              <v-list-item>
                {{ comment.created_at | yyyyMMdd }}
              </v-list-item>
            </v-list-item-content>
            <v-btn color="warning" fab x-small dark @click="updateComment()">
              수정
            </v-btn>
            <v-btn
              color="error"
              fab
              x-small
              dark
              @click="deleteComment(comment)"
            >
              삭제
            </v-btn>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "ArticleComment",
  props: {
    article_pk: Number,
  },
  data() {
    return {
      comment_content: "",
      comments: [],
      user: [],
    };
  },
  created() {
    this.commentList();
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
    commentList() {
      const config = this.getToken();
      http
        .get(`/articles/comment/list/${this.$route.params.id}`, config)
        .then(({ data }) => {
          console.log(data);
          this.comments = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    commentCreate() {
      const config = this.getToken();

      const commentItem = {
        content: this.comment_content,
      };
      if (commentItem.content) {
        http
          .post(
            `/articles/comment/create/${this.$route.params.id}/`,
            commentItem,
            config
          )
          .then(() => {
            this.commentList();
            this.comment_content = "";
          });
      }
    },
    // updateComment(comment) {
    //   const config = this.getToken();
    //   http
    //     .put(
    //       `/articles/comment/update/${this.$route.params.id}/${comment.id}/`,
    //       config
    //     )
    //     .then(({ data }) => {
    //       console.log(data);
    //       if (data.message) {
    //         alert("본인이 작성한 댓글만 수정 가능합니다!");
    //       } else {
    //         this.commentList();
    //       }
    //     });
    // },
    deleteComment(comment) {
      const config = this.getToken();
      http
        .delete(
          `/articles/comment/delete/${this.$route.params.id}/${comment.id}/`,
          config
        )
        .then(({ data }) => {
          if (data.message) {
            alert("삭제 권한이 없습니다!");
          } else {
            this.commentList();
          }
        });
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
.container {
  margin-top: 4rem;
}
.commentform {
  width: 75%;
  margin: 0px auto;
  margin-top: 5rem;
  margin-bottom: 10rem;
}
.commentbtn {
  margin-top: 3rem;
}
.card-comment {
  width: 75%;
  margin: 0 auto;
}
</style>
