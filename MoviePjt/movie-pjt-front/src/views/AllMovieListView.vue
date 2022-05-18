<template>
  <div class="all">
      <v-bottom-navigation
          color="white"
          width="450px"
          style="
            border-radius: 10px;
            background-color:cadetblue;
            text-align: center;
          "
        >
        <v-btn value="red" @click="typered">
          <span class="fs-3">최신 개봉일순</span>
        </v-btn>

        <v-btn value="white" @click="typewhite">
          <span class="fs-3">인기순</span>
        </v-btn>

        <v-btn value="rose" @click="typerose">
          <span class="fs-3">Rose</span>
        </v-btn>

        <v-btn value="sparkling" @click="typesparkling">
          <span class="fs-3">Sparkling</span>
        </v-btn>

        <v-btn value="port" @click="typeport">
          <span class="fs-3">Port</span>
        </v-btn>

      </v-bottom-navigation>

<template v-if="winelistIsEmpty">
        <div class="justify-center mt-15" style="display: flex">
          <img
            src="../assets/no_movie.png"
            style="width: 70px; height: 65px"
            alt="empty"
          />
          <h2 class="ml-5 mt-3 mb-15 pb-15">
            조회하신 영화가 없습니다. 다른 영화를 검색해주세요.
          </h2>
        </div>
      </template>
      <v-row   v-else>
        <div
          class="col-xl-3 col-lg-4 col-md-6"
          :key="i"
          v-for="(wine, i) in calData"
        >
          <v-card
            class="mx-auto mt-10"
            max-width="380"
            style="
              border-radius: 80px;
              height: 530px;
              color: gainsboro;
              background-color: #232320;
              box-shadow: 0 0 10px grey;
            "
            hover
            outlined
          >
            <v-btn
              class="mt-7 ml-15"
              text
              icon
              large
              :color="
                wine.color == 'white'
                  ? 'green lighten-3'
                  : wine.color == 'red'
                  ? 'red'
                  : wine.color == 'rose'
                  ? 'red lighten-3'
                  : wine.color == 'port'
                  ? 'blue lighten-3'
                  : 'purple lighten-2'
              "
            >
              <v-icon>mdi-circle</v-icon> {{ wine.color }}
            </v-btn>
            <v-img
              :src="wine.image"
              height="300"
              alt="No image"
              contain
              @click="winedetail(wine.wine_id)"
            /><v-img />
            <hr
              style="border-width: 2px; border-color: pink; margin-bottom: -5px"
            />
            <v-card-title class="justify-center"
              >[{{ wine.winery }}]</v-card-title
            >
            <v-card-text
              class="text-center fs-5"
              style="margin-top: -12px; color: gainsboro"
              >{{ wine.wine }}<br />
              <br />
            </v-card-text>
            <div
              class="d-flex justify-content-between align-items-center"
            ></div>
          </v-card>
        </div>
      </v-row>
      <v-row>
        <v-pagination
          v-model="currentPage"
          :length="numOfPages"
          :total-visible="10"
          style="margin-top: 10px; margin-bottom: 10px"
        ></v-pagination>
      </v-row>


    </div>
</template>