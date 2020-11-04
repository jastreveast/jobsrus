<template>
  <nav>
    <router-link to="/" exact>Job Search</router-link>
    <router-link to="profile" exact>Profile</router-link>
    <router-link to="#" exact>Career advice</router-link>
  </nav>
</template>

<script>
export default {
  name: "navBar",
};
</script>

<style lang="scss" scoped>
nav {
  background: var(--grey);
  padding: 0 200px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  border-bottom: 10px solid var(--primary);
}
 

a {
  text-decoration: none;
  color: black;
  flex: 1;
  text-align: center;
  padding: 12px;
}

.router-link-active {
  background: var(--primary);
  color: white;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

@media all and (max-width: 740px) {
  nav {
    display: none;
  }
}
</style>
