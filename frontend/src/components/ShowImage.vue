<template>
  <div>
    <img :src="expression">
  </div>
</template>

<script>
export default {
  name: 'ShowImage',
  props: {
    n: {
      type: Number,
      default: 0
    }
  },
  computed: {
    expression: function () {
      const index = (this.n > 4) ? 4 : this.n;  // 用用意してい画画が0~4なので4を超超えないように制する
      return require(`@/assets/business_man_${index}.png`)
    }
  },
  data() {
    return {
    }
  }
}
</script>