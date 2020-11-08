<template>
  <div>
    <free-bar />
    <head-bar />
    <nav-bar />
    <search-bar />
    <job-bar />
    <category-bar />
    <info-bar />
    <footer-bar />
  </div>
</template>

<script>
import headBar from "@/components/headBar.vue";
import navBar from "@/components/navBar.vue";
import freeBar from "@/components/freeBar.vue";
import searchBar from "@/components/searchBar.vue";
import infoBar from "@/components/infoBar.vue";
import footerBar from "@/components/footerBar.vue";
import categoryBar from "@/components/categoryBar.vue";
import jobBar from "@/components/jobBar.vue";

export default {
  name: "Home",
  components: {
    headBar,
    navBar,
    freeBar,
    searchBar,
    jobBar,
    infoBar,
    categoryBar,
    footerBar,
  },
};
</script>

<style lang="scss" scoped></style>
