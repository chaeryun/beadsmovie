<template>
  <div class="header">
    <div>
      <h1 class="main-title">Beads Movie</h1>
    </div>
    <div class="header-summary">
      <span>Movie &nbsp;&nbsp;</span>
      <span>Article &nbsp;&nbsp;</span>
      <span>Interest &nbsp;&nbsp;</span>
      <span>Subscribe &nbsp;&nbsp;</span>
      <span>MyPage &nbsp;&nbsp;</span>
      <span>LogOut &nbsp;&nbsp;</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "SnsHeader",

  data: () => ({}),
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");

.header {
  text-align: center;
  margin-top: 4.7rem;
  font-size: 2.5rem;
  margin-top: 2.7rem;
  margin-bottom: 2rem;
}
.main-title {
  font-family: "Amatic SC", cursive;
}
.header-summary {
  margin-top: 1rem;
  font-size: 2.5rem;
  font-family: "Amatic SC", cursive;
}
</style>
