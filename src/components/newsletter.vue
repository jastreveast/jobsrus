<template>
    <div class="container">
        <h3>Receive new jobs for this search by email</h3>
        <div class="mail">
            <input type="email" placeholder="Email">
            <button>Create Job Alert</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "newsletter",
    }
</script>

<style lang="scss" scoped>
.container {
    text-align: center;
    background-color: var(--grey);
    border: 1px solid black;

    & > h3 {
        margin-bottom: 20px;
    }
}
.mail {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

input[type="email"] {
  padding: 12px;
  font-size: 1em;
  border: 1px solid var(--grey);
  border-radius: 3px;
  width: 100%;
  flex: 2;
  margin-right: 20px;

  &:focus {
    outline: none;
  }
}

button {
  padding: 12px;
  color: white;
  border: none;
  background: var(--secondary);
  font-size: 1em;
  border-radius: 3px;
  flex: 1;
  flex-shrink: 2;
}
</style>