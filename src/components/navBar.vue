<template>
  <header>
    <div class="wrapper">
      <img src="@/assets/logo.png" alt="logo" />
      <div>
        <a href="#">Sign in</a>
        |
        <a href="#">Register</a>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "navBar",
};
</script>

<style lang="scss" scoped>
@media (min-width: 640px) {
}

@media (min-width: 768px) {
}

@media (min-width: 1024px) {
  header {
    display: grid;
    grid-template-columns: auto 1140px auto;
    grid-template-rows: auto;
  }

  .wrapper {
    grid-column-start: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 80px;

    & > img {
      height: 80px;
    }
  }
}


</style>
