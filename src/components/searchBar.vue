<template>
  <div class="container">
    <nav class="container-item">
      <router-link class="container-link" to="/" exact>Job Search</router-link>
      <router-link class="container-link" to="#" exact>Profile</router-link>
      <router-link class="container-link" to="#" exact
        >Career advice</router-link
      >
    </nav>
  </div>
</template>

<script>
export default {
  name: "searchBar",
};
</script>

<style lang="scss" scoped>
.container {
  display: grid;
  grid-template-columns: auto 1140px auto;
  background-color: rgb(247, 247, 247);

  &-item {
    grid-column-start: 2;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
  }

  &-link {
    padding: 12px 0;
    text-align: center;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    text-decoration: none;
    color: black;
  }
}

.router-link-active {
  background-color: #0d3880;
  color: white;
}
</style>
