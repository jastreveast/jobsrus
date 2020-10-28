<template>
  <div class="container"></div>
</template>

<script>
export default {
  name: "freeBar",
};
</script>

<style lang="scss" scoped>
.container {
    height: 20px;
    background: var(--grey);
}

@media all and (max-width: 740px) {
  .container {
    display: none;
  }
}
</style>
