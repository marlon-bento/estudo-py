<script setup>
const props = defineProps(['title', 'description', 'button'])
const emit = defineEmits(['tryAgain'])
</script>

<template>
<div  class="alert alert-warning alert-dismissible" role="alert">
        <div class="d-flex">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24"
                    viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                    stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M12 9v2m0 4v.01"></path>
                    <path d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75">
                    </path>
                </svg>
            </div>
            <div>
                <h4 class="alert-title">{{ props.title }}</h4>
                <div class="text-secondary">{{ props.description }}</div>
                <div class="btn-list">
                    <a @click.prevent="$emit('tryAgain')" href="#" class="btn btn-success">{{ props.button }}</a>
                </div>
            </div>
        </div>
        <a class="btn-close" data-bs-dismiss="alert" aria-label="close"></a>
    </div>
</template>
<style>


</style>
<style scoped>

</style>