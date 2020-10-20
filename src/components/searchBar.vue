<template>
  <div class="main-container">
    <b-container class="search">
      <b-row>
        <b-col
          class="position-relative d-flex justify-content-center search-tab"
        >
          <router-link class="search-link" to="/" exact>Job Search</router-link>
        </b-col>

        <b-col
          class="position-relative d-flex justify-content-center search-tab"
        >
          <router-link class="search-link" to="#" exact>Profile</router-link>
        </b-col>

        <b-col
          class="position-relative d-flex justify-content-center search-tab"
        >
          <router-link class="search-link" to="#" exact>Career</router-link>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "searchBar",
};
</script>

<style lang="scss" scoped>
.main-container {
  background-color: rgb(247, 247, 247);
}

.search {
  &-link {
    color: black;
    text-decoration: none;
    height: 100%;
    padding: 12px 0;
    text-align: center;
    width: 100%;
    height: 100%;
    border-top-right-radius: 3px;
    border-top-left-radius: 3px;

    &:hover {
      text-decoration: none;
    }
  }

  &-tab {
    padding: 0;
  }
}

.router-link-active {
  background-color: #0d3880;
  color: white;
}
</style>
