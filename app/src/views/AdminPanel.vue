<template>
  <v-layout>
    <v-flex xs6 sm6 md6 lg6>
      <UsersList :users="data" @updateData="getUsersList" />
    </v-flex>
    <v-flex xs6 sm6 md6 lg6>
      <AddNewUser @updateData="getUsersList" />
    </v-flex>
  </v-layout>
</template>
<script>
import axios from "axios";
import UsersList from "../components/AdminPanel/UsersList";
import AddNewUser from "../components/AdminPanel/AddNewUser";
export default {
  name: "AdminPanel",
  components: {
    UsersList,
    AddNewUser
  },
  data() {
    return {
      data: []
    };
  },
  methods: {
    getUsersList() {
      axios
        .get(`http://localhost:8080/users/getall`)
        .then(response => {
          this.data = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getUsersList();
  }
};
</script>