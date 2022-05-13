<template>
  <div>
    <div class="image-box">
      <carousel :autoplay="true" :nav="false" :dots="true" :autoplayHoverPause="true" :items='1'>
        <div class="jb-wrap">
          <div class="slide"></div>
          <h1 class="jb-title">신비한 동물들과<br> 덤블도어의 비밀</h1>
          <p class="jb-summary"><br><br>1930년대, 제2차 세계대전에 마법사들이 개입하게 되면서 강력한 어둠의 마법사 그린델왈드의 힘이 급속도로 커진다. 덤블도어는 뉴트 스캐맨더에게 위대한 마법사 가문 후손, 마법학교의 유능한 교사, 머글 등으로 이루어진 팀에게 임무를 맡긴다. 이에 뉴트와 친구들은 머글과의 전쟁을 선포한 그린델왈드와 추종자들, 그의 위험한 신비한 동물들에 맞서 세상을 구할 거대한 전쟁에 나선다. <br><br>장르 : 판타지, 모험<br>별점 : 6.8</p>
        </div>
        <div class="jb-wrap">
          <div class="slide2"></div>
          <h1 class="jb-title">닥터스트레인지: <br>대혼돈의 멀티버스</h1>
          <p class="jb-summary"><br><br>끝없이 균열되는 차원과 뒤엉킨 시공간의 멀티버스가 열리며 오랜 동료들, 그리고 차원을 넘어 들어온 새로운 존재들을 맞닥뜨리게 된 ‘닥터 스트레인지’. 대혼돈 속, 그는 예상치 못한 극한의 적과 맞서 싸워야만 하는데…. <br><br>장르 : 액션, 판타지, 모험<br>별점 : 7.7</p>
        </div>
        <div class="jb-wrap">
          <div class="slide3"></div>
          <h1 class="jb-title">듄</h1>
          <p class="jb-summary">10191년, 아트레이데스 가문의 후계자인 폴은 시간과 공간을 초월해 과거와 미래를 모두 볼 수 있고, 더 나은 미래를 만들 유일한 구원자인 예지된 자의 운명을 타고났다. 그리고 어떤 계시처럼 매일 꿈에서 아라키스의 행성에 있는 한 여인을 만난다. 귀족들이 지지하는 아트레이데스 가문에 대한 황제의 질투는 폴과 그 일족들을 죽음이 기다리는 아라키스로 이끄는데... <br><br>장르 : 모험, 드라마, SF<br>별점 : 8.82</p>
        </div>
        <div class="jb-wrap">
          <div class="slide4"></div>
          <h1 class="jb-title">메이의 새빨간 비밀</h1>
          <p class="jb-summary">엄마의 착한 딸, 아니면 미운 13살? 성적도 우수하고 친구들과 사이도 좋은 데다 부모와도 친밀한 관계를 유지하고 있는, 똑 부러지면서도 엉뚱한 매력의 소유자 메이는 요즘 질풍노도의 시기를 겪느라 고민이 많다. 그런데 이 와중에 흥분하면 거대한 레서판다로 변신하는 비밀까지 떠안게 되다니! 아침도 먹어야 하고 학교도 가야 하는데, 이 엄청난 비밀을 어떻게 숨겨야 할까? <br><br>장르 : 애니메이션, 가족, 코미디, 판타지<br>별점 : 7.5</p>
        </div>
        <div class="jb-wrap">
          <div class="slide5"></div>
          <h1 class="jb-title">리디밍 러브</h1>
          <p class="jb-summary">누구나 품을 수 있지만, 누구도 소유할 수 없는 ‘엔젤’ 단 한 번도 원하는 삶을 살아본 적 없던 그녀에게 운명처럼 오직 그녀를 사랑하는 남자가 나타난다 무조건적인 그의 사랑에 ‘엔젤’은 매번 도망치지만 조금씩, 그리고 천천히 진정한 세상을 알아가는데… 사랑이 이끄는 순간, 눈부신 기적이 시작된다! <br><br>장르 : 멜로/로맨스, 드라마<br>별점 : 7.0</p>
        </div>
        <div class="jb-wrap">
          <div class="slide6"></div>
          <h1 class="jb-title">나일 강의 죽음</h1>
          <p class="jb-summary">행복한 신혼부부를 태운 나일 강의 초호화 여객선
 그곳에서 끔찍한 살인 사건이 벌어진다.
 
 위태롭고 불길한 분위기의 선상에서 탑승객들을 심문하는 탐정 ‘에르큘 포와로’
 모두가 범인으로 의심되는 가운데,
 연이어 발생한 살인 사건은 그의 영혼을 송두리째 뒤흔들고,
 관객은 마지막 순간까지 예기치 못한 반전으로 놀라운 결말에 이르게 된다. <br><br>장르 : 범죄, 드라마, 미스터리 <br>별점 : 7.17</p>
        </div>
      </carousel>
    </div>

    <!-- Top 10 Movies -->

    <v-card-title
      style="
        margin-left: 190px;
        margin-top: 50px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Top 10 Movies
    </v-card-title>
    <!--<MovieCard :movies="top_movies"/>--> 
  <!--
    <v-card
        max-width="100%"
        elevation="10"
        min-width="300px"
        min-height="400px"
        style= "background-size: cover; border-radius: 0px; background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0)40%, rgba(0,0,0,0)), url(https://www.themoviedb.org/t/p/w220_and_h330_face/g4tMniKxol1TBJrHlAtiDjjlx4Q.jpg) center center ;"
      >
          <v-card-subtitle class="pb-0" >
          <h2 style="color:#fff" >배신의 만찬</h2>
          <h2></h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="white" text @click="detail"> 상세보기 </v-btn>
          <v-btn color="white" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    -->

    <v-container style="display: flex; justify-content: space-between; ">
    <carousel :autoplay="false" :nav="false" :dots="false"  :items="3" >
      <template slot="prev"><v-icon class="prev" large>mdi-chevron-left</v-icon></template>
      <template slot="next"><v-icon class="next" large>mdi-chevron-right</v-icon></template>
      <v-card
        
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px;"
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="https://mblogthumb-phinf.pstatic.net/MjAyMDEwMDJfMTE4/MDAxNjAxNjA5OTI1MDkx.iGd-vZulv298Brk8HAmipq10gf0OjKULrFpaqfagCh0g.02yjTFQ0NaVI3Wztsn6nKxGU5ePYKrNmnA0K3E2B_lsg.JPEG.cubase777/MV5BMDk5Yzc4NzMtODUwOS00NTdhLTg2MjEtZTkzZjc0ZWE2MzAwXkEyXkFqcGdeQXVyMTA3MTA4.jpg?type=w800"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>수퍼 소닉 (2020)</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>

      <v-card
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px;"
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/9Xd459BvOLFfPPzNfAPT9dZkO1x.jpg"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>웨스트 사이드 스토리</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>

      <v-card
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px; "
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/hsOhOcX7qDy7bPwbrt1OoITngrf.jpg"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>메이의 새빨간 비밀</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>
      

      
      <v-card
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px; "
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="https://blog.kakaocdn.net/dn/II2OM/btrpoVuvWts/b9rK1lvjxUFVox60anaKmK/img.png"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>엔칸토: 마법의 세계 (2021)</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>

      <v-card
        max-width="300px"
        min-width="300px"
        min-height="300px"
        elevation="10"
        style="border-radius: 0px; margin: 0px 20px 0px 20px; "
      >
        <v-img
          class="white--text align-end"
          min-width="300px"
          max-width="150px"
          max-height="430px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/wFjboE0aFZNbVOF05fzrka9Fqyx.jpg"
        >
        </v-img>
        <div class="text">
          <v-card-subtitle class="pb-0">
            <h2>애덤 프로젝트</h2>
          </v-card-subtitle>
          <v-card-actions >
            <v-btn color="orange" text> 상세보기 </v-btn>
            <v-btn color="orange" text> 찜하기 </v-btn>
          </v-card-actions>
        </div>
      </v-card>
      
    </carousel>
    </v-container>

    <!-- Action -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Action
    </v-card-title>
    <MovieCard :movies="action_movies" />
    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/bCz71ysciwNL2xddSm25ufrgZ7V.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>더 배트맨</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://mblogthumb-phinf.pstatic.net/MjAyMDEwMDJfMTE4/MDAxNjAxNjA5OTI1MDkx.iGd-vZulv298Brk8HAmipq10gf0OjKULrFpaqfagCh0g.02yjTFQ0NaVI3Wztsn6nKxGU5ePYKrNmnA0K3E2B_lsg.JPEG.cubase777/MV5BMDk5Yzc4NzMtODUwOS00NTdhLTg2MjEtZTkzZjc0ZWE2MzAwXkEyXkFqcGdeQXVyMTA3MTA4.jpg?type=w800"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>수퍼 소닉 (2020)</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/voddFVdjUoAtfoZZp2RUmuZILDI.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>스파이더맨 : 노 웨이 홈</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/nOYyuJ2mNo6RWsFsTwApEyG3F4J.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>야차</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    <!-- Animation -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Animation
    </v-card-title>
    <MovieCard :movies="animation_movies" />
    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3eElpVmCeMqplQbkQd0y1fftL04FkfbQZrjKbEuhg3D6rQuKf"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>아이스 에이지: 벅의 대모험 (2022)</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/78JfwRiubwX87BYgPXsdFKBf9P5.jpg"
        >
        </v-img>
        <v-card-subtitle class="pb-0">
          <h2>pil</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/hsOhOcX7qDy7bPwbrt1OoITngrf.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메이의 새빨간 비밀</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://blog.kakaocdn.net/dn/II2OM/btrpoVuvWts/b9rK1lvjxUFVox60anaKmK/img.png"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>엔칸토: 마법의 세계 (2021)</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    <!-- Comedy -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Comedy
    </v-card-title>
    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/wFjboE0aFZNbVOF05fzrka9Fqyx.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>애덤 프로젝트</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/r97txZRmBb75SGsIAWqmplWJnO3.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메탈 로드</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/edYk5TSowZIDv138bCpF5ls3XI5.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>더 버블</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>루프 라페타</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    <!-- Romance -->
    <v-card-title
      style="
        margin-left: 400px;
        margin-top: 30px;
        font-family: NewWaltDisney;
        font-size: 60px;
      "
    >
      Romance
    </v-card-title>

    <v-container style="display: flex">
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/iABPzTM6r5gfvnSmD7z0LblW71s.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>메리 미</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/thqgzBPEDYQX0taszVus5nYMtTZ.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>문 샷</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/vdgUNCruHI6jX9TU4vvplgpDtL7.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>배틀 : 프리스타일</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
      <v-card
        class="mx-auto"
        max-width="400"
        elevation="10"
        style="border-radius: 10px"
      >
        <v-img
          class="white--text align-end"
          height="370px"
          width="350px"
          src="https://www.themoviedb.org/t/p/w220_and_h330_face/9Xd459BvOLFfPPzNfAPT9dZkO1x.jpg"
        >
        </v-img>

        <v-card-subtitle class="pb-0">
          <h2>웨스트 사이드 스토리</h2>
        </v-card-subtitle>
        <v-card-actions>
          <v-btn color="orange" text> 상세보기 </v-btn>
          <v-btn color="orange" text> 찜하기 </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import MovieCard from "@/components/movie/MovieCard";
import carousel from "vue-owl-carousel";

export default {
  name: "MovieMain",

  data: function () {
    return {
      movies: [],
      movie: "",
    };
  },

  components: {
    MovieCard,
    carousel,
  },

  methods: {
    detail() {
      this.$router.push({ name: "MoveDetail" });
    },
    getMovieDatas: function () {
      axios.get(`https://beadsmovie.com/api/movie/`).then((res) => {
        console.log(res);
        if (this.$store.state.movies.length === 0) {
          this.$store.state.movies = res.data;
        }
      });
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap");
@font-face {
  font-family: "NewWaltDisney";
  src: url(../../fonts/NewWaltDisney.ttf) format("truetype");
}
@font-face {
  font-family: 'NanumSquareLight';
  src: url(../../fonts/NanumSquareL.ttf) format('truetype');
}
@font-face {
  font-family: 'NanumSquare';
  src: url(../../fonts/NanumSquareR.ttf) format('truetype');

}
@font-face {
  font-family: 'NanumSquareBold';
  src: url(../../fonts/NanumSquareB.ttf) format('truetype');

}
@font-face {
  font-family: 'NanumSquareExtraBold';
  src: url(../../fonts/NanumSquareEB.ttf) format('truetype');

}

.mx-auto {
  margin-top: 2rem;
}


.image-box {
  margin: -25px auto;
}
.image-thumbnail {
  margin: -100px auto;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.title {
  display: flex;

  align-items: flex-end;
}
.text {
  text-align: center;
  justify-content: center;
  font-family:  "NanumSquareExtraBold";
}

.slide{
  position: relative;
  width:100vw; height:100vh;
  background: url('@/assets/harrypotter.jpg') center no-repeat;
  background-size:cover; 
}
.slide:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));
}

.slide2{
  position: relative;
  width:100vw; height: 100vh;
  background: url('@/assets/strange.jpg') center no-repeat;
  background-size:cover; 
}
.slide2:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));

}

.slide3{
  position: relative;
  width:100vw; height: 100vh;
  background: url('@/assets/dune.jpg') center no-repeat;
  background-size:cover; 
}
.slide3:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));

}
.slide4{
  position: relative;
  width:100vw; height: 100vh;
  background: url('@/assets/red2.jpg') center no-repeat;
  background-size:cover; 
}
.slide4:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));

}
.slide5{
  position: relative;
  width:100vw; height: 100vh;
  background: url('@/assets/love.jpg') center no-repeat;
  background-size:cover; 
}
.slide5:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));

}
.slide6{
  position: relative;
  width:100vw; height: 100vh;
  background: url('@/assets/death.jpg') center no-repeat;
  background-size:cover; 
}
.slide6:after {
  content:"";
  position: absolute;
  display: block; width:100%; height:100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7),rgba(0,0,0,0));

}


.jb-wrap {
  position:relative;
}
.jb-title {
  position:absolute;
  box-sizing: content-box;
  width: 400px;
  top: 12%;
  left:5%;
  color: white;
  font-family: "NewWaltDisney", "NanumSquareExtraBold";
  font-size:50px;

}
.jb-summary {
  position:absolute;
  box-sizing: content-box;
  width: 420px;
  top:25%;
  left:5%;
  color: white;
  font-family: "NanumSquare";
  font-size:20px;
}
.prev {
  position: absolute;
  top: -10%;
  left: 60%;
}
.next {
  position: absolute;
  bottom: 104%;
  left: 62%
}

</style>
