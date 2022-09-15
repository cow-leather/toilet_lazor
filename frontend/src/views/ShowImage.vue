<template>
  <div>
    <h1 id="number" class="number">{{ n }}</h1>
    <ExpressionImage :n="n"></ExpressionImage>
  </div>
</template>

<script>
import ExpressionImage from '../components/ExpressionImage.vue'

export default {
  name: 'ShowImage',
  components: {
    ExpressionImage
  },
  data() {
    return {
      n: 1
    }
  }
}
</script>
<style>
.number {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>