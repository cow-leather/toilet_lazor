<template>
  <div>
    <img :src="expressions[index]">
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
  data() {
    return {
      index: 0,
      expressions: [
        require('@/assets/business_man_0.png'),
        require('@/assets/business_man_1.png'),
        require('@/assets/business_man_2.png'),
        require('@/assets/business_man_3.png'),
        require('@/assets/business_man_4.png')
      ]
    }
  },
  watch: {
    name(n) {
      if (n > 4) {
        this.index = 4
      } else {
        this.index = n
      }
    }
  }
}
</script>