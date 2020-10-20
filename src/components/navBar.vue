<template>
  <div class="main-container">
    <b-container>
      <b-row align-h="between">
        <b-col cols="4">
          <img src="@/assets/logo.png" alt="" style="height: 60px;" />
        </b-col>
        <b-col cols="4" class="d-flex justify-content-end">
          <div class="d-flex align-items-center">
            <b-link>Register</b-link>

            <b-link>Sign in</b-link>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "navBar",
};
</script>

<style scoped>
.main-container {
  background-color: white;
  width: 100%;
  padding: 20px 0;
}
</style>
