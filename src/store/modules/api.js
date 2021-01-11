import axios from "axios";

export default {
  namespaced: true,

  state: {
    jobs: [],
  },

  mutations: {
    updateJobs(state, payload) {
      state.jobs = payload;
    },
  },

  actions: {
    fetchJobs({ commit }, payload) {
      axios.post("/job_search", payload).then((response) => {
        const jobs = response.data.jobs;
        commit("updateJobs", jobs);
      });
    },

    fetchNext({ commit, state}) {
      const what = state.jobs.what;
      const where = state.jobs.where;
      const payload = { what, where };
      axios.post(state.jobs.next_records_url, payload).then((response) => {
        const jobs = response.data.jobs;
        console.log("got some jobs");
        commit("updateJobs", jobs);
      });
    },
  },

  getters: {
    getJobs(state) {
      return state.jobs;
    },

    getPages(state) {
      return state.pages;
    },

    getCurrentPage(state) {
      return state.currentPage;
    },

    getNext(state) {
      return state.has_next;
    },

    getPrev(state) {
      return state.has_prev;
    },
    hasJobs(state) {
      return state.jobs.length > 1 ? true : false;
    },
  },
};
