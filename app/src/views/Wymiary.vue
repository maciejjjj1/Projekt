<template>
  <div class="parametry">
  <v-card>
    <v-card-title>
      Parametry koni z naszej hodowli
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
        :headers="headers"
        :items="parametry"
        :search="search"
    ></v-data-table>

  </v-card>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Parametry",
  data() {
    return {
      search: '',
      parametry: [],
      headers: [
      { text: 'Nazwa', value: 'kon' },
      { text: 'Wzrost', value: 'wzrost' },
      { text: 'Popręg', value: 'popreg' },
      { text: 'Nadpęcie', value: 'nadpecie' }
      ]
    };
  },
  methods: {
     getParametry() {
      axios.get('http://127.0.0.1:8000/horses/parameters', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then(response => this.parametry = response.data);
          console.log(this.parametry)
    }
},
  mounted() {
    this.getParametry();
    console.log(this.parametry)
  }
}
</script>
<style scoped>
.test {
  font-size: 30px;
  color: green;
}
</style>