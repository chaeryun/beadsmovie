<template>
  <div class="container my-5">
    <!-- 검색창 -->
    <div class="d-flex mb-5">
      <input class="form-control" @input="newkeyword=$event.target.value" type="text" :value="keyword" @keyup.enter="toSearch(newkeyword)">
      <button class="btn btn-success mx-3" @click="toSearch(newkeyword)">search</button>
    </div>
    <hr class="text-white">
    <div v-if="movies.length">
      <h3 class="text-white mx-3">"{{ keyword }}"에 대한 검색 결과입니다.</h3>
      <movie-list class="mt-5" :movies="movies"></movie-list>
    </div>
    <div v-else class="d-flex justify-content-center">
      <img src="@/assets/sad.png" width="70%" alt="">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movie/MovieList.vue'

export default {
  name: 'Search',
  data: function () {
    return {
      keyword: null,
      newkeyword: null,
      movies: [],
    }
  },
  components: {
    MovieList,
  },
  methods: {
    toSearch: function (newkeyword) {
      if (newkeyword != null) {
        this.$router.go(this.$router.push({ name: 'Search', params: {keyword: newkeyword} }))
      }
    }
  },
  created: function () {
    this.keyword = this.$route.params.keyword
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/search/${this.keyword}/`,
    })
      .then((res) => {
        // console.log(this.keyword)
        this.movies = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>