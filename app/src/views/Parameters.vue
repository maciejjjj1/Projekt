<template>
  <div>
    <v-layout>
      <SingleParameterCard
        :allParameters="parameters"
        class="singleCard"
        @updateParameterList="getParameters"
      />
      <v-flex>
        <NewParameter @updateParameterList="getParameters" />
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import axios from "axios";
import NewParameter from "../components/Parameters/NewParameter";
import SingleParameterCard from "../components/Parameters/SingleParameterCard";

export default {
  name: "parameters",
  components: {
    NewParameter,
    SingleParameterCard
  },
  props: {
    allParameters: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    getParameters() {
      axios
        .get("http://localhost:8080/parameters")
        .then(response => {
          this.parameters = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  data() {
    return {
      parameters: []
    };
  },
  mounted() {
    this.getParameters();
  }
};
</script>
<style scoped>
.singleCard {
  display: flex;
  flex-wrap: wrap;
}
</style>
