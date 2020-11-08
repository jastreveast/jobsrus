import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    jobs: [{
      "id": 1,
      "locations": "South Africa",
      "site": "",
      "date": "Fri, 06 Nov 2020 08:54:26 GMT",
      "url": "http://jobviewtrack.com/en-za/job-124d416e410d010744154c432c001a06456d150608144f593f694c100e4e6a154e020f041c65264c1d0600104b471d604c0a0e09420622200408000e064118482d125e4a3f604c0a0e09420621505f555654/7ff05ebdad2a83c9ca8b15c93023f260.html?affid=213e213hd12344552",
      "title": "Clinical Data Manager",
      "description": "Clinical Data Manager - Bloemfontein   Who We Are   Synteract is a global full-service contract research organization with a successful three-decade track record supporting biotechnology, medical device and pharmaceutical companies. With ou...",
      "company": "Synteract",
      "salary": ""
    },
    {
      "id": 2,
      "locations": "South Africa",
      "site": "",
      "date": "Fri, 06 Nov 2020 08:52:36 GMT",
      "url": "http://jobviewtrack.com/en-za/job-1f4d416e410d010744154c4338130100174119050c0128685144430d0c0f4b76701107061c06084d111a68401d1f051e/2f04b9d358b42bcad77820b6963de9f6.html?affid=213e213hd12344552",
      "title": "Clinical Programmer",
      "description": "Clinical Programmer - Bloemfontein   Who We Are   Synteract is a global full-service contract research organization with a successful three-decade track record supporting biotechnology, medical device and pharmaceutical companies. With our ...",
      "company": "Synteract",
      "salary": ""
    },
    {
      "id": 3,
      "locations": "South Africa",
      "site": "",
      "date": "Fri, 06 Nov 2020 08:34:40 GMT",
      "url": "http://jobviewtrack.com/en-za/job-1f4d416e410d010744154c4338130100174119050c0128685144430d0c0f4b76701107061c06084d111a68401d1f051e/e58bb5974a4219c9bb8a9bb33c2c9fff.html?affid=213e213hd12344552",
      "title": "Clinical Programmer",
      "description": "Clinical Programmer - Bloemfontein   Who We Are   Synteract is a global full-service contract research organization with a successful three-decade track record supporting biotechnology, medical device and pharmaceutical companies. With our ...",
      "company": "Synteract",
      "salary": ""
    }],
    access_token: localStorage.getItem("access_token") || null,
  },
  mutations: {
    updateJobs(state, payload) {
      state.jobs = payload;
    },
  },

  actions: {
    fetchJobs({commit}, payload) {
      axios
        .post("/job_search", payload)
        .then((response) => {
          const jobs = response.data.jobs
          commit('updateJobs', jobs)
        });
    },
  },

  getters: {
    getJobs(state) {
      return state.jobs;
    }
  },

  modules: {},
});
