<template>
  <div>
    <h1 id="number" class="number">{{ n }}</h1>
    <ExpressionImage :n="n"></ExpressionImage>
  </div>
</template>

<script>
import ExpressionImage from '../components/ExpressionImage.vue'
import { req1 } from "../functions/req.js"

export default {
  name: 'ShowImage',
  components: {
    ExpressionImage
  },
  data() {
    return {
      n: 0,
      obj: {}
    }
  },
  methods: {
    getReq: async function () {
      this.obj = await req1()
      this.n = Number(this.obj["num"])
      console.log(typeof (this.n))
    }
  },
  created() {
    this.getReq()
  },

}
</script>
<style>
.number {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>