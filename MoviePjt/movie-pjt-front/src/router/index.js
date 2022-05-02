import Vue from "vue";
import VueRouter from "vue-router";
import MovieView from "../views/MovieView.vue";
import MovieDetail from "../components/movie/MovieDetail.vue";

import AccountView from "@/views/AccountView.vue";
import AccountSignup from "@/components/accounts/AccountSignup.vue";
import AccountLogin from "@/components/accounts/AccountLogin.vue";
import ArticleList from "@/components/articles/ArticleList.vue"; 
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
    path: "/accounts",
    name: "AccountView",
    component: AccountView,
    redirect: "/accounts/login",
    children: [
      {
        path: "login",
        name: "AccountLogin",
        component: AccountLogin,
      },
      {
        path: "signup",
        name: "AccountSignup",
        component: AccountSignup,
      },
    ],
  },

  {
    path: "/moviedetail",
    name: "MoveDetail",
    component: MovieDetail,
  },

  {
    path: "/article",
    name: "ArticleList",
    component: ArticleList,
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
