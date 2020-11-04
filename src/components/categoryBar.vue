<template>
  <section class="main">
    <nav>
      <ul>
        <li>
          <a
            href="#"
            v-bind:class="{ active: isActive('category') }"
            @click.prevent="setActive('category')"
            >Jobs by category</a
          >
        </li>
        <li>
          <a
            href="#"
            v-bind:class="{ active: isActive('cities') }"
            @click.prevent="setActive('cities')"
            >Jobs by cities</a
          >
        </li>
        <li>
          <a
            href="#"
            v-bind:class="{ active: isActive('popular') }"
            @click.prevent="setActive('popular')"
            >Popular searches</a
          >
        </li>
        <li>
          <a
            href="#"
            v-bind:class="{ active: isActive('title') }"
            @click.prevent="setActive('title')"
            >Jobs by title</a
          >
        </li>
      </ul>
    </nav>

    <div class="tab-container">
      <div
        class="tab-panel"
        id="category"
        v-bind:class="{ show: isActive('category') }"
      >
        <div class="tab-panel-col">
          <a href="#">IT & Telecommunications</a>
          <a href="#">Banking, Finance, Insurance, Stockbrocking</a>
          <a href="#">Engineering, Technical</a>
          <a href="#">Accounting, Auditing</a>
          <a href="#">Sales & Purchasing</a>
        </div>

        <div class="tab-panel-col">
          <a href="#">IT & Telecommunications</a>
          <a href="#">Banking, Finance, Insurance, Stockbrocking</a>
          <a href="#">Engineering, Technical</a>
          <a href="#">Accounting, Auditing</a>
          <a href="#">Sales & Purchasing</a>
        </div>
        <div class="tab-panel-col">
          <a href="#">IT & Telecommunications</a>
          <a href="#">Banking, Finance, Insurance, Stockbrocking</a>
          <a href="#">Engineering, Technical</a>
          <a href="#">Accounting, Auditing</a>
          <a href="#">Sales & Purchasing</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "categoryBar",

  data: function() {
    return {
      activeItem: "category",
    };
  },

  methods: {
    isActive(menuItem) {
      return this.activeItem === menuItem;
    },

    setActive(menuItem) {
      this.activeItem = menuItem;
    },
  },
};
</script>

<style lang="scss" scoped>
.main {
  background: var(--grey);
  padding: 20px 200px;
}

nav > ul {
  list-style-type: none;

  & > li {
    display: inline-block;
    padding: 12px;
    color: var(--primary);

    & > a {
      color: var(--primary);
      text-decoration: none;
    }
  }
}

.active {
  border-bottom: 2px solid var(--primary);
}

.tab-container {
  padding-top: 30px;
  padding-left: 12px;
  height: 250px;
}

.tab-panel {
  display: none;
  flex-direction: row;
  justify-content: space-between;

  &-col {
    & > a {
      font-size: 1em;
      font-weight: 300;
      text-decoration: none;
      color: var(--primary);
      display: block;
      margin-bottom: 12px;
    }
  }
}

.show {
  display: flex;
}
</style>
