import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Parameters from "./views/Parameters.vue";
import Statistics from "./views/Statistics.vue";
import AdminPanel from "./views/AdminPanel.vue";
import LoginForm from "./components/LoginForm";
import Parametry from "./views/Wymiary.vue";
import Bonitacja from "./views/Bonitacja.vue";
import Oceny from "./views/Oceny.vue";
import Recommendations from "./views/Recommendations.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/home",
      name: "Lista koni",
      component: Home,
    },
    {
      path: "/parametry",
      name: "Parametry",
      component: Parametry,
    },
    {
      path: "/bonitacja",
      name: "Bonitacja",
      component: Bonitacja,
    },
    {
      path: "/oceny",
      name: "oceny",
      component: Oceny,
    },

    {
      path: "/parameters",
      name: "parameters",
      component: Parameters,
    },
    {
      path: "/statistics",
      name: "statistics",
      component: Statistics,
    },
    {
      path: "/recommendations",
      name: "recommendations",
      component: Recommendations,
    },
    {
      path: "/login",
      name: "login",
      component: LoginForm,
    },
    {
      path: "/admin",
      name: "admin",
      component: AdminPanel,
    },
  ],
});
