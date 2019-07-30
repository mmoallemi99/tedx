import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueResource from 'vue-resource';
Vue.use(VueResource);

Vue.config.productionTip = false;

import './assets/css/styles.css';
import './assets/css/new_css.css';
import './assets/css/responsive.css';

window.$ = require('jquery');
window.JQuery = require('jquery');

new Vue({
  assetsPublicPath: '/vueapp/',
  router,
  render: h => h(App),
}).$mount('#app');
