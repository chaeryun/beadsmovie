import Vue from "vue";
import VueRouter from "vue-router";
import MovieView from "../views/MovieView.vue";
import MovieDetail from "../components/movie/MovieDetail.vue";
import MovieList from "../components/movie/Movielist.vue";

import AccountView from "@/views/AccountView.vue";
import AccountSignup from "@/components/accounts/AccountSignup.vue";
import AccountLogin from "@/components/accounts/AccountLogin.vue"; 

import ArticleView from "@/views/ArticleView.vue";
import ArticleList from "@/components/articles/ArticleList.vue";
import ArticleCreate from "@/components/articles/ArticleCreate.vue";
import ArticleDetail from "@/components/articles/ArticleDetail.vue";
import ArticleUpdate from "@/components/articles/ArticleUpdate.vue";
import ArticleDelete from "@/components/articles/ArticleDelete.vue";
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
    name: "MovieDetail",
    component: MovieDetail,
  },
  {
    path: "/movielist",
    name: "MovieList",
    component: MovieList,
  },

  {
    path: "/article",
    name: "ArticleView",
    component: ArticleView,
    redirect: "/article/list",
    children: [
      {
        path: "list",
        name: "ArticleList",
        component: ArticleList,
      },
      {
        path: "create",
        name: "ArticleCreate",
        component: ArticleCreate,
      },
      {
        path: "detail/:id",
        name: "ArticleDetail",
        component: ArticleDetail,
      },
      {
        path: "update/:id",
        name: "ArticleUpdate",
        component: ArticleUpdate,
      },
      {
        path: "delete/:id",
        name: "ArticleDelete",
        component: ArticleDelete,
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
