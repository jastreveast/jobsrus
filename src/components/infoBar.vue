<template>
  <section>
    <img src="@/assets/phone.svg" alt="" />
    <div class="main">
      <h1>Find jobs on the GO</h1>
      <p>with our mobile app, on IOS and Android</p>
      <a href="#">Download our mobile app now</a>
      <div class="logos">
        <img src="@/assets/apple.svg" alt="apple app store" />
        <img src="@/assets/google.svg" alt="google play store" />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "infoBar",
};
</script>

<style lang="scss" scoped>
section {
  background: var(--primary);
  padding: 0 200px;
  height: 300px;
  position: relative;
  z-index: 500;
  display: flex;

  & > img {
    position: absolute;
    bottom: 0;
    left: 200px;
    height: 350px;
  }
}

.main {
  text-align: left;
  margin-left: 500px;
  margin-top: auto;
  margin-bottom: auto;

}

.logos {

    & > img {
        display: inline-block;
        height: 40px;
        margin-top: 20px;
        margin-right: 20px;
    }
}

h1 {
  color: white;
  font-size: 2em;
}

p {
  color: white;
  font-size: 1.5em;
}

a {
  color: var(--action);
  font-size: 1em;
  text-decoration: none;
}

@media all and (max-width: 740px) {
  section {
    display: block;
    text-align: center;
  }
}
</style>
