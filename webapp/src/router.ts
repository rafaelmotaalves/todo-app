import { createWebHistory, createRouter } from "vue-router";
import Board from "./components/Board.vue";

const routes = [
  {
    path: "/boards/:id",
    name: "Home",
    component: Board,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;