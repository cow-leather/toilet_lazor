<template>
  <div>
    <h1 id="number" class="number">{{ n }}</h1>
    <h1>{{ raise_n }}</h1>
    <ExpressionImage :n="n"></ExpressionImage>
  </div>
</template>

<script>
import ExpressionImage from '../components/ExpressionImage.vue'
import { req1, req2 } from "../functions/req.js"

export default {
  name: 'ShowImage',
  components: {
    ExpressionImage
  },
  data() {
    return {
      n: 0,
      raise_n: 0,
      obj: {},
      raise_obj: {}
    }
  },
  methods: {
    getReq: async function () {
      this.obj = await req1()
      this.n = Number(this.obj["num"])
      console.log(typeof (this.n))
    },
    getRaise: async function () {
      this.raise_obj = await req2()
      this.raise_n = Number(this.raise_obj["num"])
      console.log(this.raise_n)
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