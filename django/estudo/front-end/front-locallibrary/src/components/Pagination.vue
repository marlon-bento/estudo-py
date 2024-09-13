<script setup>
const props = defineProps(['next', 'previous', 'count'])



import { computed } from 'vue';

// Calcular a página atual com base na prop `previous`
let current // = computed(() => props.previous == null ? 1 : props.previous + 1);



</script>
<template>
   {{ props.previous }}
</template>