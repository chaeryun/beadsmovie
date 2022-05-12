<template>
  <div @click="toDetail(movie)" class="card text-white" style="width: 18%; height: 485px; background-color: rgba(50, 60, 65, 0.9)">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body d-flex align-items-start flex-column">
      <p class="card-title fw-bold fs-6 mb-auto">{{ movie.title }}</p>
      <p class="my-0 align-text-bottom">{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YY.MM.DD') }}</p>
      <p class="my-0 align-text-bottom">★ {{ movie.vote_average }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  data: function () {
    return {
      poster: null,
    }
  },
  props: {
    movie: Object
  },
  methods: {
    toDetail: function (movie) {   
        this.$router.push({ name: 'MovieDetail', params: {movieId: movie.id} })   
    },
  },
  created: function () {
    this.poster = `https://www.themoviedb.org/t/p/w440_and_h660_face/${this.movie.poster_path}`
  }
}
</script>

<style>

</style>