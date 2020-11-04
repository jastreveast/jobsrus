<template>
  <div>
    <free-bar />
    <head-bar />
    <nav-bar />
    <profile-bar/>
  </div>
</template>

<script>
import headBar from "@/components/headBar.vue";
import navBar from "@/components/navBar.vue";
import freeBar from "@/components/freeBar.vue";
import profileBar from "@/components/profileBar.vue";


export default {
  name: "Home",
  components: {
    headBar,
    navBar,
    freeBar,
    profileBar,
    
  },
};
</script>

<style lang="scss" scoped></style>
