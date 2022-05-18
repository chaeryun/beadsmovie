<template>
  <v-container class="mypages">
    <v-row align="center" justify="center">
      <h1>Mypage</h1>
    </v-row>

    <!-- <v-row class="uploadimage" align="center" justify="center">
      <image-input v-model="avatar">
        <div slot="activator">
          <v-avatar
            size="150px"
            v-ripple
            v-if="!avatar"
            class="grey lighten-3 mb-3"
          >
            <span>Click to add avatar</span>
          </v-avatar>
          <v-avatar size="150px" v-ripple v-else class="mb-3">
            <img :src="avatar.imageURL" alt="avatar" />
          </v-avatar>
        </div>
      </image-input>
      <!-- <v-slide-x-transition>
        <div v-if="avatar && saved == false">
          <v-btn class="primary" @click="uploadImage" :loading="saving"
            >Save Avatar</v-btn
          >
        </div>
      </v-slide-x-transition> -->
    </v-row> -->

    <!-- <v-row align="center" justify="center">
      <v-slide-x-transition>
        <div v-if="avatar && saved == false">
          <v-btn class="primary" @click="uploadImage" :loading="saving"
            >이미지 저장</v-btn
          >
        </div>
      </v-slide-x-transition>
    </v-row> -->

    <v-row align="center" justify="center">
      <span class="usercontent">{{ this.user.nickname }}</span>
    </v-row>

    <v-row class="mt-4" align="center" justify="center">
      <br />
      <span class="userfunction" @click="deleteuser"><img src="../../assets/cry.png"><h4>회원탈퇴</h4></span>
    </v-row>
  </v-container>
</template>

<script>
import ImageInput from "@/components/accounts/ImageInput.vue";
import http from "@/util/http-common";
import jwt_decode from "vue-jwt-decode";
import { mapState, mapMutations } from "vuex";

export default {
  name: "AccountMypage",

  components: {
    ImageInput,
  },
  data: () => ({
    user: "",

    // image
    avatar: null,
    saving: false,
    saved: false,
  }),

  watch: {
    avatar: {
      handler: function () {
        this.saved = false;
      },
      deep: true,
    },
  },

  computed: {
    ...mapState({
      userstate: (state) => state.user.isLogin,
    }),
  },

  created() {
    // user data 불러오기
    this.getuser();
  },

  methods: {
    ...mapMutations("user", ["SET_USER_STATE"]),

    getToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `jwt ${token}`,
        },
      };
      return config;
    },

    // get user data
    async getuser() {
      const config = this.getToken();
      const hash = localStorage.getItem("jwt");
      // console.log(VueJwtDecode.decode(hash));
      const info = jwt_decode.decode(hash);
      await http.post(`/accounts/myprofile/`, info, config).then(({ data }) => {
        this.user = data;
      });
    },

    // delete user
    async deleteuser() {
      const config = this.getToken();
      const userid = this.user.id;
      await http
        .delete(`/accounts/delete/${userid}`, config)
        .then(({ data }) => {
          console.log(data);
          alert("정상적으로 탈퇴되었습니다.");

          this.SET_USER_STATE(false);
          localStorage.removeItem("jwt");
          this.$router.push({ name: "home" });
        });
    },

    // image upload
    uploadImage() {
      this.saving = true;
      setTimeout(() => this.savedAvatar(), 1000);
      console.log("avatar", this.avatar);
    },
    savedAvatar() {
      this.saving = false;
      this.saved = true;
    },
  },
};
</script>

<style scoped>
.usercontent {
  font-size: 30px;
}

.userfunction {
  font-size: 30px;
}

.userfunction:hover {
  cursor: pointer;
}

.uploadimage {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.mypages{
  color: white;
}

</style>
