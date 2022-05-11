<template>
  <v-main class="pt-10 pb-10">
    <v-container class="login-page">
      <v-layout class="row wrap">
        <v-flex col-7></v-flex>
        <v-flex col-5>
          <h1 style="color: tomato">Login</h1>
          <br />

          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="user.id"
              :counter="16"
              :rules="idRules"
              label="ID"
              required
            ></v-text-field>

            <v-text-field
              v-model="user.password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              hint="At least 4 characters ~ 12 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>

            <div>
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="validate"
              >
                Login
              </v-btn>

              <v-btn color="error" class="mr-4" @click="signup"> Signup </v-btn>
            </div>

            <br />

            <!-- <div>
              <v-btn depressed tile text>
                <v-img
                  src="@/assets/kakao_login_medium_narrow.png"
                  contain
                  @click="kakaologin"
                ></v-img>
              </v-btn>
            </div> -->
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import http from "@/util/http-common";
import jwt_decode from "jwt-decode";
// import axios from "axios";
import { mapState, mapMutations } from "vuex";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Accountlogin",
  data: () => ({
    valid: false,
    // name rule
    idRules: [
      (v) => !!v || "ID is required",
      (v) =>
        (v && v.length <= 16 && v.length >= 4) ||
        "ID must be least 4 characters ~ 12 characters ",
    ],
    // password rule
    show1: false,
    rules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => 4 <= v.length <= 12 || "Max 12 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    user: {
      id: "",
      password: "",
    },
  }),

  computed: {
    ...mapState({
      userstate: (state) => state.user.isLogin,
    }),
  },

  methods: {
    ...mapMutations("user", ["SET_USER_STATE"]),

    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate() == true) {
        this.login();
      }
    },

    // general login
    async login() {
      await http({
        method: "post",
        url: "/accounts/login/",
        data: {
          username: this.user.id,
          password: this.user.password,
        },
      })
        .then((res) => {
          let token = res.data.token;
          localStorage.setItem("jwt", token);
          // this.$store.commit("SET_USER_STATE", true);
          // store 저장
          this.SET_USER_STATE(true);
          // console("userstate", this.userstate);
          console.log(res);

          // home 이동
          this.$router.push({ name: "home" }).catch((err) => err);
          let decode_token = jwt_decode(token);
          console.log("decode_token", decode_token);
          this.saveuser(decode_token.username);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    async saveuser(id) {
      await http({
        method: "POST",
        url: "/accounts/profile/" + id,
      })
        .then((res) => {
          console.log("profile", res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    signup() {
      this.$router.push({ name: "AccountSignup" });
    },

    // kakaoLogin
    kakaologin() {
      window.Kakao.Auth.login({
        scope: "account_email, gender, profile_nickname, profile_image",
        // success: this.getProfile,
        success: this.getProfile,
      });
    },

    getProfile(authObj) {
      localStorage.setItem("jwt", authObj.jwt);
      console.log("프로필 받기", authObj);

      console.log("Token : ", authObj.jwt);
      this.kakaologin2(authObj.jwt);

      // window.Kakao.API.request({
      //   url: "/v2/user/me",
      //   success: (res) => {
      //     const kakao_account = res.kakao_account;
      //     console.log("response :", res);
      //     console.log(kakao_account);
      //     // this.kakaologin2();
      //   },
      // });
    },

    async kakaologin2(token) {
      await http({
        method: "POST",
        url: "user/oauth/kakao",
        data: {
          Kakao: token,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.v-text-field {
  width: 600px;
  height: 90px;
}

.v-btn:not(.v-btn--round).v-size--default {
  padding: 0;
}

.login-page {
  /* background-image: url("../../assets/"); */
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 20px;
  padding: 150px;
  margin: auto !important;
  opacity: 0.9;
}
</style>
