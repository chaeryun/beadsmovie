<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="400" elevation="10">
          <v-img
            height="500px"
            width="400px"
            src="https://www.themoviedb.org/t/p/w220_and_h330_face/g4tMniKxol1TBJrHlAtiDjjlx4Q.jpg"
          >
          </v-img>
        </v-card>
      </v-col>

      <v-col cols="8">
        <v-card flat>
          <v-card-title class="mt-5"> <h2>배신의 만찬</h2> </v-card-title>
          <v-card-subtitle>액션 / 스릴러 </v-card-subtitle>
          <v-card-text>CIA 요원이자 전 연인(크리스 파인, 탠디 뉴턴)이 구출 임무를 실패하고 몇 년이 지난 뒤 재회하고,
            <br /> 업무와 개인적인 감정을 구분하지 못한다. 국제 스파이 행위, 도덕적 딜레마, 
            <br/> 그리고 치명적인 배신을 다룬 눈을 뗄 수 없는 이야기다.</v-card-text>
            <v-col cols="7">
        <span><h3>비슷한 영화추천</h3></span>
        <div style="display:flex">
        <v-img
          class="white--text align-end ml-10 mt-8"
          height="270px"
          width="200px"
          style="border-radius: 60px;"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/6zBWSuYW3Ps1nTfeMS8siS4KUaA.jpg"
        >
        </v-img>
        <v-img
          class="white--text align-end ml-10 mt-8"
          height="270px"
          width="200px"
          style="border-radius: 60px;"
          src="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/rqeYMLryjcawh2JeRpCVUDXYM5b.jpg"
        >
        </v-img>
        </div>
      </v-col>
        </v-card>
      </v-col>
    </v-row>

        <v-row>
      <v-col class="my-10">
          <span><h3>예고편</h3></span>
            <div style="height: 400px; background-image: url('https://i.ytimg.com/vi/6s7NziAetNs/hqdefault.jpg');">
                <a href="https://www.youtube.com/watch?v=DfQx5kfERwE"> 
                  <div style="padding-left: 200px; padding-top: 130px;"><img src="../../assets/play2.png" /></div>
                </a>
            </div>
      </v-col>
        </v-row>
      
  </v-container>
</template>

<script>
export default {
  name: "MovieDetail",
};
      
</script>

<style scoped>
</style>
