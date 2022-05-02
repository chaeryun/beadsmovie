<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="400" elevation="10">
          <v-img
            height="370px"
            width="400px"
            src="https://www.themoviedb.org/t/p/w220_and_h330_face/g4tMniKxol1TBJrHlAtiDjjlx4Q.jpg"
          >
          </v-img>
        </v-card>
      </v-col>

      <v-col cols="8">
        <v-card flat>
          <v-card-title> 배신의 만찬 </v-card-title>
          <v-card-subtitle>장르</v-card-subtitle>
          <v-card-text>내용</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="5">
        <span>예고편</span>
      </v-col>
      <v-col cols="7">
        <span>비슷한 영화추천</span>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "MovieDetail",
};
</script>

<style scoped></style>
