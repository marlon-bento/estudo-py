<script setup>
const props = defineProps(['title', 'description','button']);
const emit = defineEmits(['more']);
</script>
<template>
    <div class="alert alert-success alert-dismissible" role="alert">
        <div class="d-flex">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24"
                    viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                    stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M5 12l5 5l10 -10"></path>
                </svg>
            </div>
            <div>
                <h4 class="alert-title">{{ props.title }}</h4>
                <div class="text-secondary">{{ props.description }}</div>
                <div v-if="props.button!='none'" class="btn-list">
                    <a @click.prevent="$emit('more')" href="#" class="btn btn-success">{{ props.button }}</a>
                </div>
            </div>
        </div>
        
    </div>
</template>