<template>
  <div class="container" v-if="hasJobs">
    <newsletter/>
    <job-card
      v-for="job in getJobs"
      v-bind:key="job.id"
      :title="job.title"
      :company="job.company"
      :description="job.description"
    />
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapGetters } = createNamespacedHelpers("api");
import jobCard from "@/components/jobCard.vue";
import newsletter from "@/components/newsletter.vue";

export default {
  name: "jobBar",

  components: {
    jobCard,
    newsletter,
  },
  computed: {
    ...mapGetters(["getJobs", "hasJobs"]),
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
