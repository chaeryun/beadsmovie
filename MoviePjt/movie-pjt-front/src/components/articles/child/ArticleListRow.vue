<template>
  <router-link
    :to="{
      name: 'ArticleDetail',
      params: { id: id, user: user },
    }"
  >
    <figure class="item">
      <v-img :src="`http://127.0.0.1:8000` + image" /></figure
  ></router-link>
</template>

<script>
export default {
  name: "ArticleListRow",
  props: {
    id: Number,
    user: Number,
    image: String,
  },
  computed: {},
};
</script>

<style scoped>
.item {
  column-width: 350px;
  column-gap: 15px;
  display: inline-block;
  margin-top: 1rem;
  margin-bottom: 1rem;
  justify-content: center;
  align-items: center;
  border-radius: 1rem;
  border: 1px solid rgba(0, 0, 0, 0.2);
  padding: 10px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
}
.item img {
  column-width: 350px;
  column-gap: 15px;
  width: 100%;
  border-radius: 1rem;
}
</style>
