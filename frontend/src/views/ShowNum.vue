<template>
    <div>
        <h1 id="number" class="number">{{ n }}{{ }}</h1>
    </div>
</template>

<script>
import { req } from "../functions/req.js"
export default {
    data() {
        return {
            n: 0,
            text: ""
        }
    },
    methods: {
        getReq() {
            this.text = req()
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