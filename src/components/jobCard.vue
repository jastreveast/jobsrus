<template>
  <div class="container">
    <a href="#">{{ title }}</a>
      <h4>{{ company }}</h4>
      <p>{{ description }}</p>
      <div class="logo-bar">
          <img src="@/assets/index.png" alt="logo">
      </div>
  </div>
</template>

<script>
export default {
  name: "jobCard",
  props: ["date", "title", "description", "company" ],
};
</script>

<style lang="scss" scoped>
.container {
    padding: 20px 100px;
    background: var(--grey);
    border: 1px solid rgb(136, 136, 136);
    border-bottom: none;

    & > a {
        font-size: 1.5em;
        color: var(--link);
        text-decoration: none;
        
    }

    & > h4 {
        color: var(--primary);
        margin-top: 5px;
        margin-bottom: 20px;
    }

    .logo-bar {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;

        & > img {
            height: 60px;
            width: auto;
        }
    }


}
</style>
