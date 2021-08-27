<template>
  <v-layout class="main">
    <v-card class="userCard" v-for="user in users" v-bind:key="user.id">
      <v-toolbar color="deep-purple accent-4" dark>
        <v-toolbar-title>Name: {{user.name}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click="deleteUser(user.id)">
          <v-icon>delete</v-icon>
        </v-btn>
      </v-toolbar>
      <v-list>
        UserID: {{user.id}}
        <v-subheader>Password: {{user.password}}</v-subheader>
        <v-icon v-if="user.isAdmin">supervised_user_circle</v-icon>
      </v-list>
    </v-card>
  </v-layout>
</template>
<script>
import axios from "axios";
export default {
  name: "UsersList",
  props: {
    users: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    deleteUser(id) {
      axios
        .delete(`http://localhost:8080/users/?id=${id}`)
        .then(response => {
          console.log(response);
          this.$emit("updateData");
        })
        .catch(error => {
          console.log(error.response);
        });
    }
  }
};
</script>
<style scoped>
.main {
  flex-wrap: wrap;
  display: flex;
  align-items: center;
  justify-content: center;
}
.userCard {
  margin-top: 2%;
  width: 40vw;
}
</style>