<template>
  <section class="main">
    <img src="@/assets/profile.jpg" alt="people" />
    <div class="cards">
        
    </div>
  </section>

</template>

<script>
export default {
  name: "profileBar",
};
</script>

<style lang="scss" scoped>
.main {
  text-align: center;

  & > img {
    height: 350px;
    width: auto;
  }
}

.cards {
  display: flex;
  flex-direction: row;
}
</style>
