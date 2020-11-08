import Vue from "vue";
import NProgress from 'vue-nprogress';
import App from "./App.vue";
import router from "./router";
import store from "./store";


Vue.config.productionTip = false;
Vue.use(NProgress)
const nprogress = new NProgress()

new Vue({
  nprogress,
  router,
  store,
  render: h => h(App)
}).$mount("#app");
