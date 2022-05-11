<template>
  <v-main class="pt-10 pb-10">
    <v-container class="signup-page">
      <v-layout row wrap>
        <v-flex col-7></v-flex>
        <v-flex col-5>
          <h1 style="color: tomato">Signup</h1>
          <br />

          <v-form ref="form" v-model="valid" lazy-validation>
            <!-- <v-row>
              <v-col cols="12" sm="5">
                <v-text-field
                  v-model="user.first_name"
                  :rules="nameRules"
                  color="purple darken-2"
                  label="First name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="5">
                <v-text-field
                  v-model="user.last_name"
                  :rules="nameRules"
                  color="blue darken-2"
                  label="Last name"
                  required
                ></v-text-field>
              </v-col>
            </v-row> -->

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
              v-model="user.passwordConfirmation"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[passrules.required, passrules.min]"
              :type="show2 ? 'text' : 'password'"
              name="input-10-1"
              label="PasswordConfirm"
              hint="At least 4 characters ~ 12 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>

            <v-text-field
              v-model="user.email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>

            <v-text-field
              v-model="user.nickname"
              :rules="nicknameRules"
              label="Nickname"
              required
            ></v-text-field>

            <v-row>
              <v-col cols="12" sm="5">
                <v-slider
                  v-model="user.age"
                  color="orange"
                  label="Age"
                  min="1"
                  max="100"
                  thumb-label
                ></v-slider>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="5">
                <v-select
                  v-model="user.gender"
                  :items="genders"
                  label="Gender"
                  required
                ></v-select>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="5">
                <v-select
                  v-model="user.occupation"
                  :items="occupations"
                  label="Occupation"
                  required
                ></v-select>
              </v-col>
            </v-row>

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
                @click="validate"
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
import http from "@/util/http-common.js";

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

    // passwordConfirmation
    show2: false,
    passwordConfirmation: "",
    passrules: {
      required: (value) => !!value || "Password is Required.",
      min: (v) => (v.length <= 12 && v.length >= 4) || "Max 12 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    // email rule
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],

    // name rule
    // first_name: "",
    // last_name: "",
    // nameRules: [(val) => (val || "").length > 0 || "This field is required"],

    nickname: "",
    nicknameRules: [
      (v) => !!v || "Nickname is required",
      (v) => v.length <= 12 || "Nickname must be less than 12 characters",
    ],

    age: "",

    genders: ["male", "female"],

    occupations: ["student", "professor", "consultant", "manager", "other"],

    // select: null,
    // items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,

    user: {
      id: "",
      password: "",
      passwordConfirmation: "",
      email: "",
      nickname: "",
      age: "",
      gender: "",
      occupation: "",
    },
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      console.log(this.user.gender);

      if (this.$refs.form.validate() == true) {
        this.regist();
      }
    },

    // 회원가입
    async regist() {
      await http({
        method: "POST",
        url: "accounts/signup/",
        data: {
          username: this.user.id,
          password: this.user.password,
          passwordConfirmation: this.user.passwordConfirmation,
          email: this.user.email,
          nickname: this.user.nickname,
          age: this.user.age,
          sex: this.user.gender,
          occupation: this.user.occupation,
        },
      })
        .then((res) => {
          console.log(res);
          alert("회원가입 성공");
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
