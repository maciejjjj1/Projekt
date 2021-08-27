<template>
  <div class="bonitacja">
  <v-card>
    <v-card-title>
        Bonitacja koni z naszej hodowli
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
        :items="bonitacja"
        :search="search"
    ></v-data-table>
<!--    <v-simple-table>-->
<!--    <template v-slot:default>-->
<!--      <thead>-->
<!--        <tr>-->
<!--          <th class="text-left">-->
<!--            Nazwa-->
<!--          </th>-->
<!--          <th class="text-left">-->
<!--            Wzrost-->
<!--          </th>-->
<!--          <th class="text-left">-->
<!--            Popręg-->
<!--          </th>-->
<!--          <th class="text-left">-->
<!--            Nadpęcie-->
<!--          </th>-->
<!--        </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--        <tr-->
<!--          v-for="item in parametry"-->
<!--          :key="item.parametry"-->
<!--        >-->
<!--          <td>{{ item.kon }} </td>-->
<!--          <td>{{ item.wzrost }}</td>-->
<!--          <td>{{item.popreg}}</td>-->
<!--          <td>{{item.nadpecie}}</td>-->
<!--        </tr>-->
<!--      </tbody>-->
<!--    </template>-->
<!--  </v-simple-table>-->
  </v-card>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Bonitacja",
  data() {
    return {
      search: '',
      bonitacja: [],
      headers: [
      { text: 'Nazwa', value: 'kon' },
      { text: 'Typ', value: 'typ' },
      { text: 'Głowa z szyją', value: 'glowa' },
      { text: 'Nogi przednie', value: 'noga_przod' },
      { text: 'Nogi tylne', value: 'noga_tyl' },
      { text: 'Kopyta', value: 'kopyta' },
      { text: 'Stęp', value: 'step' },
      { text: 'Kłus', value: 'klus' },
      { text: 'Wrażenie ogólne', value: 'ogolny' },
      { text: 'Razem', value: 'razem' }
      ]
    };
  },
  methods: {
     getBonitacja() {
      axios.get('http://127.0.0.1:8000/horses/valuation', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then(response => this.bonitacja = response.data);
          console.log(this.bonitacja)
    }
},
  mounted() {
    this.getBonitacja();
    console.log(this.bonitacja)
  }
}
</script>
<style scoped>
.test {
  font-size: 10px;
  color: green;
}
</style>