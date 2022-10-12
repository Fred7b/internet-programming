import Vue from 'vue'
import App from './App.vue'
import 'popper.js';
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import axios from 'axios'
Vue.prototype.$http = axios;


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
