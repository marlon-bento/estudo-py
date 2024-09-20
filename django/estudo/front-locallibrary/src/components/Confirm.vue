<script setup>
const emit = defineEmits(['yes','no'])
</script>
<template>
    <div class=" model bg-red  text-light d-flex p-6 flex-column  justify-content-between justify-content-center">
        <p class="display-6">Realmente deseja excluir os dados?</p>
        <div class="">
            <button @click="$emit('yes',true)" class="btn btn-success me-3">yes</button>
            <button @click="$emit('no',false)" class="btn btn-dark">no</button>
        </div>
    </div>
</template>
<style scoped>
.model{
    position: absolute;
    display: block;
    bottom: 20px;
    left: 50%;
    z-index: 20;
    border-radius: 6px;
    max-width: 100%;
    width: 600px;
    height: 300px;
    padding: 2px 10px;
    margin: 0 auto;
    text-align: center;
    transform: translate(-50%,-50%);
}
</style>