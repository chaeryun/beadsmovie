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

            <div>
              <v-btn depressed tile text>
                <v-img
                  src="@/assets/kakao_login_medium_narrow.png"
                  contain
                  @click="kakaologin"
                ></v-img>
              </v-btn>
            </div>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
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

  computed: {},

  methods: {
    validate() {
      this.$refs.form.validate();
    },

    signup() {
      this.$router.push({ name: "AccountCreate" });
    },

    // kakaoLogin
    kakaologin() {
      window.Kakao.Auth.login({
        scope: "account_email, gender, profile_nickname, profile_image",
        success: this.getProfile,
      });
    },

    getProfile(authObj) {
      // console.log("프로필 받기", authObj);
      sessionStorage.setItem("access_token", authObj.access_token);
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: (res) => {
          const kakao_account = res.kakao_account;
          console.log("response :", res);
          console.log(kakao_account);
        },
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
</style>
