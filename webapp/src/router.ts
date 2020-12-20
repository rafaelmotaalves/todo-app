import { createWebHistory, createRouter } from "vue-router";
import Board from "./components/Board.vue";
import Home from "./components/Home.vue"

const routes = [
    {
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/boards/:id",
        name: "board",
        component: Board,
        props: true
    }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;