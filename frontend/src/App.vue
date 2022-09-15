<template>
  <BekkuHeader></BekkuHeader>
  <nav>
    <router-link to="/">expression</router-link> |
    <router-link to="/signal">signal</router-link> |
    <router-link to="/number">number</router-link>
  </nav>
  <router-view />
  <BekkuFooter></BekkuFooter>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import BekkuFooter from "./components/BekkuFooter.vue"
import BekkuHeader from "./components/BekkuHeader.vue"

export default {
  components: {
    BekkuFooter,
    BekkuHeader,
  },
}
</script>

