<template>
  <section class="container">
    <form class="container-form" action="#">
      <label for="what">What</label>
      <input id="what" type="text" placeholder="Enter keywords">
      <label for="where">Where</label>
      <input type="text" placeholder="Enter city or town">
      <button>Seek</button>
    </form>
  </section>
</template>

<script>
export default {
  name: "formBar",
};
</script>

<style scoped lang="scss">
.container {
  display: grid;
  grid-template-columns: auto 1140px auto;
  background-color: #0d3880;
  padding: 40px;
  align-items: center;
  

  &-form {
    grid-column-start: 2;
    display: grid;
    grid-template-columns: 2fr 2fr 0.5fr;
    grid-template-rows: auto auto;

    & > input[type="text"] {
      grid-row-start: 2;
      font-size: 1em;
      padding: 12px 12px;
      border: none;
      margin-right: 10px;
    };
  }
}

button {
  grid-row-start: 2;
  background: #e60278;
  border: none;
  border-radius: 3px;
  color: white;
  font-size: 1em;
  
}

label { 
  color: white;
  margin-bottom: 5px;
}
</style>
