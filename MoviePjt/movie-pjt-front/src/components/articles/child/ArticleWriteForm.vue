<template>
  <div class="writeform">
    <v-form @submit="onSubmit">
      <v-card>
        <v-toolbar flat color="blue-grey" dark>
          <v-toolbar-title>글 작성</v-toolbar-title>
        </v-toolbar>

        <v-card-text>
          <v-text-field
            ref="title"
            filled
            outlined
            label="글 제목"
            placeholder="제목 입력..."
            v-model="article.title"
          ></v-text-field>

          <v-textarea
            ref="content"
            filled
            outlined
            label="글 내용"
            placeholder="내용 입력..."
            v-model="article.content"
          ></v-textarea>

          <v-file-input ref="image" label="File input" v-model="article.image">
            <template v-slot:selection="{ text }">
              <v-chip small label color="primary">
                {{ text }}
              </v-chip>
            </template></v-file-input
          >
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            v-if="this.type === 'register'"
            type="submit"
            color="success"
            depressed
            x-large
          >
            글 작성
          </v-btn>
          <v-btn v-else type="submit" color="success" depressed x-large>
            글 수정
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleWriteForm",
  data() {
    return {
      article: {
        title: "",
        content: "",
        image: [],
      },
    };
  },
  props: {
    type: { type: String },
  },
  created() {
    if (this.type === "modify") {
      try {
        axios
          .get(
            `http://127.0.0.1:8000/api/articles/detail/${this.$route.params.id}/`
          )
          .then(({ data }) => {
            this.article.title = data.title;
            this.article.content = data.content;
          });
      } catch (err) {
        alert("데이터를 읽어오지 못했습니다 !!");
      }
    }
  },
  methods: {
    getToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    onSubmit(event) {
      event.preventDefault();

      let err = true;
      let msg = "";

      !this.article.title &&
        ((msg = "제목을 입력해주세요 !"),
        (err = false),
        this.$refs.title.focus());
      err &&
        !this.article.content &&
        ((msg = "내용을 입력해주세요 !"),
        (err = false),
        this.$refs.content.focus());
      err &&
        this.article.image.length === 0 &&
        ((msg = "이미지를 첨부해주세요 !"),
        (err = false),
        this.$refs.image.focus());

      if (!err) alert(msg);
      else
        this.type === "register" ? this.registArticle() : this.modifyArticle();
    },
    async registArticle() {
      const config = this.getToken();
      const formData = new FormData();
      formData.append("title", this.article.title);
      formData.append("content", this.article.content);
      formData.append("image", this.article.image);
      try {
        await axios
          .post(`http://127.0.0.1:8000/api/articles/create/`, formData, config)
          .then(({ data }) => {
            let msg = "등록 처리시 문제가 발생했습니다.";
            if (data !== null) {
              msg = "등록이 완료되었습니다.";
            }
            alert(msg);
            this.moveList();
          });
      } catch (err) {
        console.log(err);
      }
    },
    async modifyArticle() {
      const config = this.getToken();
      const formData = new FormData();
      formData.append("title", this.article.title);
      formData.append("content", this.article.content);
      formData.append("image", this.article.image);
      try {
        axios
          .put(
            `http://127.0.0.1:8000/api/articles/update/${this.$route.params.id}/`,
            formData,
            config
          )
          .then(({ data }) => {
            let msg = "등록 처리시 문제가 발생했습니다.";
            if (data !== null) {
              msg = "등록이 완료되었습니다.";
            }
            alert(msg);
            this.moveList();
          });
      } catch (err) {
        console.log(err);
      }
    },
    moveList() {
      this.$router.push({ name: "ArticleList" });
    },
  },
};
</script>

<style scoped>
.writeform {
  width: 75%;
  margin: 0px auto;
  margin-top: 5rem;
  margin-bottom: 10rem;
}
</style>
