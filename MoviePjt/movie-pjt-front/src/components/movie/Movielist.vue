<template>
  <div>
    <!-- 검색결과 5개 이하 -->
    <div v-if="movies.length <= 5" class="carousel-item active">
      <div class="d-flex justify-content-around">
        <movie-list-item
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        >
        </movie-list-item>
      </div>
    </div>
    <!-- 검색결과 5개 초과 -->
    <div v-else class="d-flex flex-wrap">
      <div v-for="movie in movies" :key="movie.id" @click="toDetail(movie)" class="card mx-2 my-3" style="width: 18%;">
        <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-title fw-bold fs-6">{{ movie.title }}</p>
          <p>★ {{ movie.vote_average }}</p>
          <p>{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YY.MM.DD') }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/movie/MovieListItem.vue'
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  props: {
    movies: Array
  },
  methods: {
    toDetail: function (movie) {
       this.$router.push({ name: 'MovieDetail', params: {movieId: movie.id} }) 
    }
  }
}
</script>

<style>

</style>