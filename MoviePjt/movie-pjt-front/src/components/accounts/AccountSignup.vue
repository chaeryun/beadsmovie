<template>
  <v-main class="pt-10 pb-10">
    <v-container class="signup-page">
      <v-layout row wrap>
        <v-flex col-7></v-flex>
        <v-flex col-5>
          <h1 style="color: tomato">Signup</h1>
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

            <v-text-field
              v-model="user.nickname"
              :counter="8"
              :rules="nicknameRules"
              label="Nickname"
              required
            ></v-text-field>

            <v-checkbox
              v-model="checkbox"
              :rules="[(v) => !!v || 'You must agree to continue!']"
              label="개인정보 수집 및 이용에 동의합니다."
              required
            ></v-checkbox>
            <div>
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="regist"
              >
                Signup
              </v-btn>

              <v-btn color="error" class="mr-4" @click="reset"> Cancel </v-btn>
            </div>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>
<script>
// import http from "@/util/http-common.js";
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "AccountSignup",
  data: () => ({
    valid: false,
    // name rule
    id: "",
    idRules: [
      (v) => !!v || "ID is required",
      (v) => (v && v.length <= 16) || "ID must be less than 16 characters",
    ],

    // password rule
    show1: false,
    password: "",
    rules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => (v.length <= 12 && v.length >= 4) || "Max 12 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    // nickname rule
    nickname: "",
    nicknameRules: [
      (v) => !!v || "Nickname is required",
      (v) =>
        (v && v.length <= 16) || "Nickname must be less than 16 characters",
    ],

    // select: null,
    // items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,

    user: {
      id: "",
      password: "",
      nickname: "",
    },
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.from.validate() == true) {
        this.regist();
      }
    },

    // 회원가입
    async regist() {
      await axios({
        method: "POST",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: {
          username: this.user.id,
          password: this.user.password,
          passwordConfirmation: this.user.password,
          age: this.user.nickname,
        },
      })
        .then((res) => {
          console.log(res);
          // this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    reset() {
      this.$router.push({ name: "login" });
    },
  },
};
</script>

<style scoped>
.v-text-field {
  width: 600px;
  height: 90px;
}
</style>
