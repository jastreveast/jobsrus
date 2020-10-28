<template>
  <div>
    <free-bar />
    <head-bar />
    <div class="stick">
      <nav-bar />
      <search-bar />
    </div>
    <info-bar />
    <footer-bar/>
  </div>
</template>

<script>
import headBar from "@/components/headBar.vue";
import navBar from "@/components/navBar.vue";
import freeBar from "@/components/freeBar.vue";
import searchBar from "@/components/searchBar.vue";
import infoBar from "@/components/infoBar.vue";
import footerBar from "@/components/footerBar.vue";

export default {
  name: "Home",
  components: {
    headBar,
    navBar,
    freeBar,
    searchBar,
    infoBar,
    footerBar
  },
};
</script>

<style lang="scss" scoped>
.stick {
  position: sticky;
  top: 0;
}
</style>
