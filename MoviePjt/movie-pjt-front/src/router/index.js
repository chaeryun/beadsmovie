import Vue from "vue";
import VueRouter from "vue-router";
import MovieView from "../views/MovieView.vue";

import AccountView from "@/views/AccountView.vue";
import AccountCreate from "@/components/account/AccountCreate.vue";
import AccountLogin from "@/components/account/AccountLogin.vue";
// import User from "../views/User.vue";
// import Userlogin from "@/components/user/login.vue";
// import Signup from "@/components/user/signup.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: MovieView,
  },
  {
    path: "/account",
    name: "AccountView",
    component: AccountView,
    redirect: "/account/login",
    children: [
      {
        path: "login",
        name: "AccountLogin",
        component: AccountLogin,
      },
      {
        path: "create",
        name: "AccountCreate",
        component: AccountCreate,
      },
    ],
  },

  // {
  //   path: "/user",
  //   name: "User",
  //   component: User,
  //   children: [
  //     {
  //       path: "login",
  //       name: "login",
  //       component: Userlogin,
  //     },
  //     {
  //       path: "signup",
  //       name: "signup",
  //       component: Signup,
  //     },
  //   ],
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
