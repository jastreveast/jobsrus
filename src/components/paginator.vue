<template>
  <div>
    <button class="previous">Prev</button>
    <button></button>
    <button class="next" @click="fetchNext">next</button>
  </div>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapGetters } = createNamespacedHelpers("api");

export default {
  name: "paginator",
  computed: {
    ...mapGetters(["getPages"]),
  },
  methods: {
    fetchNext() {
      this.$emit("fetch-next");
    },
  },
};
</script>

<style lang="scss" scoped>
* {
  font-size: 18px;
  color: var(--primary);
}
</style>
