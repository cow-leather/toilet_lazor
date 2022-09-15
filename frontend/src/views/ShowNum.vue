<template>
    <div>
        <h1 id="number" class="number">{{ n }}</h1>
    </div>
</template>

<script>
export default {
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