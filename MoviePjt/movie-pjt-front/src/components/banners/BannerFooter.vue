<template>
  <div class="footer">
    <div class="footer-summary">
            <span>김채련</span> | <span>심은조</span> | <span>양승우</span> | <span>이윤영</span> | <span>황이레</span>  
    </div>
    <div class="footer-title">
      <h3>Beads Movie</h3>
    </div>
    <div class="footer-title">
      <h1></h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "BannerFooter",

  data: () => ({}),
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");

.footer {
  text-align: center;
  margin-top: 2rem;
}
.footer-summary {
  font-size: 0.8rem;
  color: grey;
}
.footer-title {
  margin-top: 1rem;
  font-family: "Amatic SC", cursive;
  color: darkgrey;
}
</style>
