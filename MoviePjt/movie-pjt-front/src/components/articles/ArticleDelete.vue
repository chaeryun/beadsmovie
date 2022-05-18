<template>
  <v-container class="bv-example-row mt-3">
    <v-row>
      <v-col>
        <v-alert><h3>글 목록</h3></v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col><v-alert>삭제처리중...</v-alert></v-col>
    </v-row>
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "ArticleDelete",
  created() {
    const config = this.getToken();
    try {
      http
        .delete(`/articles/delete/${this.$route.params.id}/`, config)
        .then(({ data }) => {
          let msg = "삭제 처리시 문제가 발생했습니다.";
          if (data !== null) {
            msg = "삭제가 완료되었습니다.";
          }
          alert(msg);
          this.$router.push({ name: "ArticleList" });
        });
    } catch (err) {
      alert("데이터를 읽어오지 못했습니다 !!");
    }
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
  },
};
</script>

<style></style>
