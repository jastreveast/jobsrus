<template>
  <section class="container-fluid">
    <div class="container d-flex justify-content-center">
      <b-form class="search-form" inline>
        <b-row class="search-form-row">
          <b-col cols="5">
            <b-input
              class="search-form-element"
              placeholder="Enter keywords"
            ></b-input>
          </b-col>
          <b-col cols="5">
            <b-input
              class="search-form-element"
              placeholder="City, town or province"
            ></b-input>
          </b-col>
          <b-col cols="2">
            <b-button class="search-form-element" variant="primary"
              >Seek</b-button
            >
          </b-col>
        </b-row>
        <b-form-group>
          <b-form-group class="pt-3">
            <b-form-checkbox-group id="checkbox-group-2" name="flavour-2">
              <b-form-checkbox class="checkbox" value="full_time"
                >Full time</b-form-checkbox
              >
              <b-form-checkbox class="checkbox" value="part_time"
                >Part time</b-form-checkbox
              >
              <b-form-checkbox class="checkbox" value="w_f_h"
                >Work from home</b-form-checkbox
              >
            </b-form-checkbox-group>
          </b-form-group>
        </b-form-group>
      </b-form>
    </div>
  </section>
</template>

<script>
export default {
  name: "formBar",
};
</script>

<style scoped lang="scss">
.container-fluid {
  background-color: #0d3880;
  padding: 50px 0;
  box-shadow: 0 0.25rem 0.25rem rgba(0, 0, 0, 0.25),
    inset 0 -1px 5px rgba(0, 0, 0, 0.25);
}

.search-form {
  width: 100%;

  &-row {
    width: 100%;
  }

  &-element {
    width: 100% !important;
  }
}

.container {
  padding: 0;
}

.checkbox {
  color: white;
}
</style>
