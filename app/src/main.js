import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router.js'
import "./plugins/datetime";
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueResource from 'vue-resource';


Vue.config.productionTip = false
Vue.use(VueAxios, axios)
new Vue({
  router,
  vuetify,
  axios,
  render: h => h(App)
}).$mount('#app')


Vue.use(VueResource);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App)
}).$mount("#app");