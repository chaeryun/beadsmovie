import Vue from "vue";
import VueRouter from "vue-router";
import MovieView from "../views/MovieView.vue";

import User from "../views/User.vue";
import Userlogin from "@/components/user/login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: MovieView,
  },

  {
    path: "/user",
    name: "User",
    component: User,
    children: [
      {
        path: "login",
        name: "login",
        component: Userlogin,
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
