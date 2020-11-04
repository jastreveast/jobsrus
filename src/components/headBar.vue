<template>
  <header>
    <div class="container">
      <img class="container-logo" src="@/assets/logo.svg" alt="logo" />
      <nav class="link-container">
        <router-link class="link" to="#">Sign in</router-link>
        <span class="space link">|</span>
        <router-link class="link" to="#">Employer site</router-link>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "headBar",
};
</script>

<style lang="scss" scoped>
header {
  background: white;
  padding: 20px 0;
}

.container {
  margin: 0 200px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  &-logo {
    height: 30px;
    width: auto;
  }
}

.space {
  margin: 0 10px;
}

.link {
  color: var(--link);
  text-decoration: none;
  font-size: 18px;
}

@media all and (max-width: 740px) {
  header {
    display: none;
  }
}
</style>
