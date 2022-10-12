import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/tasks",
      name: "task-list",
      component: () => import("./components/TasksComponent")
    },
    {
      path: "/tasks/:id",
      name: "task-details",
      component: () => import("./components/Task")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("./components/AddTask")
    }
  ]
});