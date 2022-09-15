<template>
  <div class="app">
    <h1 id="number" class="number">{{ n }}</h1>

    <div class="signal" v-bind:style="signal_color"></div>
    <button v-on:click="increse">+1</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      n: 0,
      color: ["Lime", "GreenYellow", "yellow", "orange", "red"],
    };
  },
  methods: {
    increse() {
      this.n++;
    },
  },
  computed: {
    signal_color() {
      return {
        backgroundColor: `${this.color[this.n]}`,
      };
    },
  },
};
</script>
<style>
.app {
  display: flex;
  align-items: center;
  justify-content: center;
}

.signal {
  justify-content: center;
  width: 150px;
  height: 150px;
  border-radius: 50%;
}
</style>
