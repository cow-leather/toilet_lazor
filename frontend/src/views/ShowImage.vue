<template>
  <div>
    <h1 id="number" class="number">{{ n }}</h1>
    <h1>{{ raise_n }}</h1>
    <div id="container">
      <!-- 0人のときは表示せず，1人増えるごとにどんどん表情が変化していく -->
      <ExpressionImage :n="n - 1" v-if="n >= 1"></ExpressionImage>
      <ExpressionImage :n="n - 2" v-if="n >= 2"></ExpressionImage>
      <ExpressionImage :n="n - 3" v-if="n >= 3"></ExpressionImage>
      <ExpressionImage :n="n - 4" v-if="n >= 4"></ExpressionImage>
      <ExpressionImage :n="n - 5" v-if="n >= 5"></ExpressionImage>
      <ExpressionImage :n="n - 6" v-if="n >= 6"></ExpressionImage>
      <ExpressionImage :n="n - 7" v-if="n >= 7"></ExpressionImage>
      <ExpressionImage :n="n - 8" v-if="n >= 8"></ExpressionImage>
      <ExpressionImage :n="n - 9" v-if="n >= 9"></ExpressionImage>
      <ExpressionImage :n="n - 10" v-if="n >= 10"></ExpressionImage>
    </div>
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
      this.raise_n = Number(this.raise_obj["raiseNum"])
      console.log(this.raise_n)
    }
  },
  created() {
    this.getReq()
    this.getRaise()
  },

}
</script>
<style>
.number {
  display: flex;
  align-items: center;
  justify-content: center;
}

#container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  place-items: center;
}
</style>