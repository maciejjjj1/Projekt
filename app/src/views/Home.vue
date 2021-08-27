<template>
 <div>
   <v-card>
     <v-card-title>
                     Witamy w bazie koni Stajni Janowo. Zapraszamy do przeglądania i dokonywania oceny!
      <v-spacer></v-spacer>
    </v-card-title>
   </v-card>
    <v-data-table
      :headers="headers"
      :items="horses"
      class="elevation-1"
    >
      <template v-slot:item.favourite="{ item }">
        <v-simple-checkbox
          v-model="item.favourite"
        ></v-simple-checkbox>
      </template>
    </v-data-table>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "listaKoni",
  data() {
    return {
      horses: [],
      headers: [
      { text: 'Nazwa', value: 'imie' },
      { text: 'Rasa koni', value: 'rasa_koni' },
      { text: 'Data urodzenia', value: 'birthday_date' },
      { text: 'Ulubione', value: 'favourite' },
      { text: 'średnia ocena', value: 'average_grade' }

      ]
    };
  },
  methods: {
     getHorses() {
      axios.get('http://127.0.0.1:8000/horses/', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then(response => this.horses = response.data);
          console.log(this.horses)
    }
},
  mounted() {
    this.getHorses();
    console.log(this.horses)
  }
}
</script>
<style scoped>
.test {
  font-size: 30px;
  color: green;
}
</style>