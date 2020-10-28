<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

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
    --primary: #0d3880;
    --secondary: rgb(226, 55, 155);
    --info: rgb(199, 234, 250);
    --link: #2765cf;
    --grey: rgb(240, 240, 240);
  }

</style>
