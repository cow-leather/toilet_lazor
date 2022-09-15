import { createRouter, createWebHistory } from "vue-router";
// import HomeView from '../views/HomeView.vue'
// import ShowNum from "../views/ShowNum.vue"
import ShowSignal from "../views/ShowSignal.vue";

const routes = [
  {
    path: "/",
    name: "shownum",
    component: ShowSignal,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
