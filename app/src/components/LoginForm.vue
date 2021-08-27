<template>

  <v-layout class="main">
    <v-container class="flex">
      <h1>MyApp</h1>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="credentials.username"
          label="Username..."
          :rules="usernameRules"
          solo
          dense
          prepend-inner-icon="star_outline"
        ></v-text-field>
        <v-text-field
          v-model="credentials.password"
          :rules="passwordRules"
          type="password"
          label="Password..."
          solo
          dense
          prepend-inner-icon="star_outline"
        ></v-text-field>
      </v-form>
      <div class="errorMsg" v-if="wrongUsernameOrPassword">Valid username or password</div>
      <div class="btnLogin">
        <v-btn class="success" @click="loginUser">Login</v-btn>
      </div>
    </v-container>
  </v-layout>
</template>
<script>
import axios from "axios";
export default {
  name: "LoginForm",
  data() {
    return {
    credentials: {
      username: null,
      password: null,
    },
      wrongUsernameOrPassword: false,
      valid: false,
      usernameRules: [v => !!v || "Login is required"],
      passwordRules: [v => !!v || "Password is required"]
    };
  },
  methods: {
    loginUser() {
      axios
          .post(
              `http://127.0.0.1:8000/api/token/`, 
              this.credentials)
          .then(response => {
            console.log(response.data);
            this.data = response.data;
            sessionStorage.setItem("token", this.data.access);
            this.$emit("updateLoggedIn");
            this.$router.push({ path: '/home' })
          })
          .catch(error => {
            console.log(error);
          });
    }
  }}

</script>
<style scoped>
.main {
  margin-top: 5%;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}
h1 {
  justify-content: center;
  display: flex;
  font-weight: 300;
  margin-bottom: 5vh;
}
.flex {
  justify-content: center;
  align-items: center;
}
.btnLogin {
  display: flex;
  align-items: center;
  justify-content: center;
}
.errorMsg {
  color: red;
}
</style>
