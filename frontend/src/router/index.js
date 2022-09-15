import { createRouter, createWebHistory } from "vue-router";
// import HomeView from '../views/HomeView.vue'
import ShowNum from "../views/ShowNum.vue";
import ShowSignal from "../views/ShowSignal.vue";
import ShowImage from '../views/ShowImage.vue'

const routes = [
  {
    path: "/",
    name: "shownum",
    component: ShowNum,
  },
  {
    path: "/signal",
    name: "signal",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: ShowSignal,
  },
  {
    path: '/expression',
    name: 'expression',
    component: ShowImage
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
