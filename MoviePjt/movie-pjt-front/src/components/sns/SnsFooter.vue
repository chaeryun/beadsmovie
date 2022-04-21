<template>
  <div class="footer">
    <div class="footer-summary">
      <span>공지사항</span> | <span>팀 소개</span> |
      <span>서비스 소개</span>
    </div>
    <div class="footer-title">
      <h3>Beads Movie</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "SnsFooter",

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
}
.footer-title {
  margin-top: 1rem;
  font-family: "Amatic SC", cursive;
}
</style>
