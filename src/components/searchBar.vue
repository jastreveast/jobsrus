<template>
  <section>
    <form>
      <div class="flex">
        <label for="what">What</label>
        <input
          v-model="what"
          id="what"
          type="text"
          placeholder="Enter keywords"
        />
      </div>
      <div class="flex">
        <label for="where">Where</label>
        <input
          v-model="where"
          id="where"
          type="text"
          placeholder="Enter town or city"
        />
      </div>
      <button @click.prevent="jobRequest">Find Jobs</button>
    </form>
  </section>
</template>

<script>
export default {
  name: "searchBar",
  data() {
    return {
      what: "",
      where: "",
    };
  },
  methods: {
    jobRequest() {
      this.$emit("job-request", this.what, this.where);
    },
  },
};
</script>

<style lang="scss" scoped>
section {
  background: var(--primary);
  padding: 60px 0;
  box-shadow: 0 0.25rem 0.25rem rgba(0, 0, 0, 0.25);

  & > form {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: flex-end;
    margin: 0 200px;
  }
}

input[type="text"] {
  padding: 12px;
  font-size: 1em;
  border: none;
  border-radius: 3px;
  width: 100%;

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

.flex {
  flex: 2;
  flex-shrink: 1;
  margin-right: 10px;
}

label {
  color: white;
  display: block;
  margin-bottom: 5px;
}

@media all and (max-width: 740px) {
  section > form {
    flex-direction: column;
    justify-content: center;
    margin: 0 20px;
  }

  .flex {
    margin-right: 0;
    margin-bottom: 5px;
    width: 100%;
  }

  button {
    width: 100%;
    margin-top: 15px;
  }
}
</style>
