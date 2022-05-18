<template>
  <v-container class="bv-example-row mt-3">
    <v-row>
      <v-col>
        <v-alert show><h3>글작성</h3></v-alert>
      </v-col>
    </v-row>
    <article-write-form type="register" />
  </v-container>
</template>

<script>
import ArticleWriteForm from "./child/ArticleWriteForm.vue";

export default {
  name: "ArticleCreate",
  components: {
    ArticleWriteForm,
  },
};
</script>

<style></style>
