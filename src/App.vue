<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap');

  * {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    height: 100vh;
  }

  :root {
    --primary: #0D2C54;
    --secondary: #F6511D;
    --action: #7FB800;
    --link: #00A6ED;
    --grey: rgb(240, 240, 240);
  }

</style>
