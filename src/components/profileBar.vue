<template>
  <section class="main">
    <form v-if="!isAuthenticated">
      <div class="employer">
        <router-link to="#">Employer?</router-link>
      </div>
      <h1>Login</h1>
      <input type="email" placeholder="Email">
      <input type="password" placeholder="password">
      <button>Login</button>
      <small>Forgot <a href="#">username or password?</a></small>
    </form>
  
  </section>

</template>

<script>
export default {
  name: "profileBar",
  computed: {
    isAuthenticated() {
      if (this.$store.access_token != undefined) {
        return true
      }
      return false
    }
  }
};
</script>

<style lang="scss" scoped>
.main {
  display: flex;
  justify-content: center;

  & > form {
    border-radius: 5px;
    width: 400px;
    display: flex;
    flex-direction: column;
    text-align: center;
    padding: 30px;
    box-shadow: 5px 5px 5px rgba($color: #000000, $alpha: 0.2), -5px -5px -5px rgba($color: #000000, $alpha: 0.2);
    border: 2px solid var(--grey);
    margin-top: 30px;

    & > h1 {
      margin-bottom: 20px;
      margin-top: 20px;
    }
  }
}

input[type="email"], input[type="password"] {
  padding: 12px;
  font-size: 1em;
  border: 1px solid var(--grey);
  border-radius: 3px;
  width: 100%;
  margin-bottom: 10px;

  &:focus {
    outline: none;
  }
}

button {
  background-color: var(--secondary);
  color: white;
  border: none;
  padding: 12px;
  font-size: 1em;
  border-radius: 4px;
}

.employer {
  display: flex;
  justify-content: flex-end;
  background: var(--grey);
  margin-left: -30px;
  margin-right: -30px;
  margin-top: -30px;
  padding: 12px 30px;
}

a {
  color: var(--link);
}

small {
  margin-top: 20px;
}

</style>
