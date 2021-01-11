import Vue from "vue";
import Vuex from "vuex";
import api from "./modules/api";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    access_token: localStorage.getItem("access_token") || null,
  },
  mutations: {},

  actions: {},

  getters: {},

  modules: {
    api,
  },
});
