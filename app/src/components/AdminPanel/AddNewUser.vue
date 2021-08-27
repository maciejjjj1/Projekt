<template>
  <v-layout class="main">
    <v-card class="card">
      <v-toolbar color="green accent-5" class="mb-5" dark>
        <v-toolbar-title>Add new user form:</v-toolbar-title>
      </v-toolbar>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="user.name"
          label="Username..."
          solo
          dense
          prepend-inner-icon="account_box"
        ></v-text-field>
        <v-text-field
          v-model="user.password"
          type="password"
          label="Password..."
          solo
          dense
          prepend-inner-icon="grade"
        ></v-text-field>
        <v-btn @click="addNewUser" class="btnAddUser success">
          <v-icon>add</v-icon>Add new user
        </v-btn>
      </v-form>
    </v-card>
  </v-layout>
</template>
<script>
import axios from "axios";
export default {
  name: "AddNewUser",
  data() {
    return {
      user: {
        name: null,
        password: null,
        isAdmin: false
      },
      valid: false
    };
  },
  methods: {
    addNewUser() {
      this.error = false;
      if (this.user.name && this.user.password) {
        axios
          .post("http://localhost:8080/users/", this.user)
          .then(resp => {
            console.log(resp.data);
            this.$emit("updateData");
            this.$refs.form.reset();
          })
          .catch(error => {
            console.log(error.response);
          });
      }
    }
  }
};
</script>
<style scoped>
.main {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 5%;
}
.card {
  width: 25vw;
  padding: 10px;
}
.btnAddUser {
  width: 100%;
}
</style>