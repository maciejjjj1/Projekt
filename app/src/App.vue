<template>
  <v-app>
    <v-content>
      <Navbar v-if="token" @updateLoggedIn="login" />
      <LoginForm v-if="!token" @updateLoggedIn="login"  />
      <router-view v-if="token"></router-view>
    </v-content>
  </v-app>

</template>

<script>
import LoginForm from "./components/LoginForm";
import Navbar from "./components/Navbar.vue";

export default {
  components: { LoginForm, Navbar },
  name: "App",
  data() {
    return {
      token: null

    };

  },
  methods: {
    login() {

      this.token = sessionStorage.getItem("token");
    }
  },
  mounted() {
    this.login();
  }
};
</script>
