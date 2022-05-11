<template>
  <v-container class="bv-example-row mt-3">
    <v-row>
      <v-col>
        <v-alert><h3>글 수정</h3></v-alert>
      </v-col>
    </v-row>
    <article-write-form type="modify" />
  </v-container>
</template>

<script>
import ArticleWriteForm from "./child/ArticleWriteForm.vue";

export default {
  name: "ArticleUpdate",
  components: {
    ArticleWriteForm,
  },
};
</script>

<style></style>
