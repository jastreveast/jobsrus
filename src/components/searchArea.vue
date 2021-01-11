<template>
  <div>
    <job-bar />
    <search-bar v-on:job-request="fetchJobs" />
    <paginator v-on:fetch-next="fetchNext"/>
  </div>
</template>

<script>
import searchBar from "@/components/searchBar.vue";
import jobBar from "@/components/jobBar.vue";
import paginator from "@/components/paginator.vue";
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("api");

export default {
  name: "searchArea",
  components: {
    searchBar,
    jobBar,
    paginator,
  },
  methods: {
    ...mapActions({
      fetch: "fetchJobs",
      fetchMore: "fetchNext",
    }),

    fetchJobs(what, where) {
      this.fetch({ what, where });
    },

    fetchNext() {
      console.log("emitted");
      this.fetchMore();
    },
  },
};
</script>

<style lang="scss" scoped></style>
