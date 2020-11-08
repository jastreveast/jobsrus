<template>
  <div class="container">
    <job-card
    v-for="job in jobs"
    v-bind:key="job.id"
    :title="job.title"
    :company="job.company"
    :description="job.description"/>
  </div>
</template>

<script>
import jobCard from "@/components/jobCard.vue";
export default {
  name: "jobBar",
  data() {
    return {
      id: 1,
    };
  },
  components: {
    jobCard,
  },
  computed: {
    jobs() {
      return this.$store.getters.getJobs;
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  background: var(--grey);
  padding: 20px 200px;
  background-color: white;
}

</style>
