<template>
  <v-app-bar app dark src="../assets/navbar.jpg" class="nav">
    <v-toolbar-title v-if="username">Hello {{username}}!</v-toolbar-title>
    <v-menu transition="slide-x-transition" bottom right>
      <template v-slot:activator="{ on }">
        <v-btn class="hidden-sm-and-up white--text" text v-on="on">
          <v-icon>add</v-icon>Menu
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="link in links" v-bind:key="link.text" :href="link.route">
          <v-list-item-title>{{ link.text }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-flex class="hidden-sm-and-down list">
      <v-btn text v-for="link in links" v-bind:key="link.text" :href="link.route">
        {{ link.text }}
        <v-icon>{{ link.icon }}</v-icon>
      </v-btn>
    </v-flex>
    <v-btn text @click="logout">
      Wyloguj
      <v-icon>logout</v-icon>
    </v-btn>
  </v-app-bar>
</template>
<script>
export default {
  data() {
    return {
      links: [
        {
          text: "Lista koni",
          route: "/home",
          icon: "star"
        },
        {
          text: "Parametry",
          route: "/parametry",
          icon: "star"
        },
        {
          text: "Bonitacja",
          route: "/bonitacja",
          icon: "signal_cellular_alt"
        },
        {
        text: "Oceny",
        route: "/oceny",
        icon: "signal_cellular_alt"
        },
        {
          text: "Polecane",
          route: "/recommendations",
          icon: "star"
        },
      ],
      username: null
    };
  },
  methods: {
    logout() {
      sessionStorage.removeItem("token");
      this.$emit("updateLoggedIn");
      this.$router.push({ path: "/login" });
    }
  },
};
</script>
<style scoped>
.nav {
  z-index: 20;
}
.list {
  justify-content: center;
  display: flex;
}
</style>
