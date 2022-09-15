<template>
  <img :src="expression">
</template>

<script>
export default {
  name: 'ExpressionImage',
  props: {
    n: {
      type: Number,
      default: 0
    }
  },
  computed: {
    expression: function () {
      let index = this.n;
      if (index > 4) {
        // 用意している画像が5枚なのでインデックスが4を超えないようにする
        index = 4;
      } else if (index < 0) {
        // インデックスが0未満にならないようにする
        index = 0;
      }
      return require(`@/assets/business_man_${index}.png`)
    }
  },
  data() {
    return {
    }
  }
}
</script>