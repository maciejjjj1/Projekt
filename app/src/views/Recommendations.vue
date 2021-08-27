<template>
	<v-container>
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
	</v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "listaKoni",
  data() {
    return {
      horses: [],
      headers: [
      { text: 'Średnia ocena', value: 'average_grade' },
      { text: 'Nazwa', value: 'imie' },
      { text: 'Rasa', value: 'rasa_koni' },
      { text: 'Data urodzenia', value: 'birthday_date' },
      ]
    };
  },
  methods: {
     getHorses() {
      axios.get('http://127.0.0.1:8000/horses/recommended', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.data)
      .then(data => {
        for(let i = 0; i < data.length; i++) {
          if (data[i].average_grade === -1) data[i].average_grade = "-----";
        }
        return data;
      })
      .then(data => this.horses = data);
    }
},
  mounted() {
    this.getHorses();
    console.log(this.horses)
  }
}
</script>