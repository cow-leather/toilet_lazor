<template>
    <div>
        <h1 id="number" class="number">{{ n }}</h1>
        <ShowImage :n="n"></ShowImage>
    </div>
</template>

<script>
import ShowImage from '../components/ShowImage.vue'

export default {
    components: {
        ShowImage
    },
    data() {
        return {
            n: 0
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