<template>

<div>
  <h1 class="text-center mt-4">Oceń konia</h1>
  <v-form v-model="valid">
    <v-container class="d-flex justify-center">
      <v-col :cols="6">
        <v-autocomplete
          v-model="selectedHorse"
          :items="horses"
          label="Imię konia"
          item-text="imie"
          item-value="id"
          required
          :rules="[v => !!v || 'Należy wybrać konia do oceny']"
        ></v-autocomplete>

        <div class="d-flex justify-center">
          <v-rating
            hover
            length="10"
            size="32"
            v-model="grade"
          ></v-rating>
        </div>

        <v-btn 
          color="success"
          :disabled="!valid"
          @click="gradeHorse"
        >Oceń</v-btn>
      </v-col>
    </v-container>
  </v-form>
</div>
</template>

<script>

import axios from "axios";

export default {
  data: function() {
    return {
      valid: true,
      horses: [],
      selectedHorse: null,
      grade: 0,
    };
  },

  methods: {
    gradeHorse() {
      axios.post("http://127.0.0.1:8000/horses/rate/" + this.selectedHorse, {
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + sessionStorage.getItem("token")
        }

      })
       .then(res => console.log(res.data))
       .catch(err => console.log(err))
      // axios.post(`http://127.0.0.1:8000/api/token/`, this.credentials)

    },
    created()
      {
        axios
            .get("http://127.0.0.1:8000/horses/")
            .then(response => {
              this.horses = response.data;
            })
            .catch(error => {
              localStorage.removeItem('token')
              console.log(error)
            })
      }},
  mounted() {
  this.created();
  }};

//
//       const data =  { grade: this.grade };
//       const cfg = {
//
//         method: 'POST',
//         headers: {
//           "Content-Type": "application/json",
//           "Authorization": "Bearer " + sessionStorage.getItem("token")
//         },
//         body: JSON.stringify(data)
//       };
//       fetch("http://127.0.0.1:8000/horses/rate/" + this.selectedHorse, cfg);
//
//     }
//   },
//
//   created() {
//     fetch("http://127.0.0.1:8000/horses/")
//     .then(res => res.json())
//     .then(res => {
//       this.horses = res;
//     });
//   }
// };

</script>