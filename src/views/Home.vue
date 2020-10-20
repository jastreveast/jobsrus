<template>
  <div>
    <nav-bar />
    <search-bar />
    <form-bar />
  </div>
</template>

<script>
import navBar from "@/components/navBar.vue";
import searchBar from "@/components/searchBar.vue";
import formBar from "@/components/formBar.vue";


export default {
  name: "Home",
  components: {
    navBar,
    searchBar,
    formBar
    
  },
};
</script>

<style scoped></style>
