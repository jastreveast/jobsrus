<template>
  <div>
    <free-bar />
    <head-bar />
    <nav-bar />
    <search-area />
    <category-bar />
    <info-bar />
    <footer-bar />
  </div>
</template>

<script>
import headBar from "@/components/headBar.vue";
import navBar from "@/components/navBar.vue";
import freeBar from "@/components/freeBar.vue";
import infoBar from "@/components/infoBar.vue";
import footerBar from "@/components/footerBar.vue";
import categoryBar from "@/components/categoryBar.vue";
import searchArea from "@/components/searchArea.vue";

export default {
  name: "Home",
  components: {
    headBar,
    navBar,
    freeBar,
    infoBar,
    categoryBar,
    footerBar,
    searchArea,
  },
};
</script>

<style lang="scss" scoped></style>
