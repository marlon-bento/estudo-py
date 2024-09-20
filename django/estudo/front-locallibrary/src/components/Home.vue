
<script setup>
    let rawHtml = "to lindo"
</script>

<template>
    <div class="text-white fs-1">
        <p>Using text interpolation: {{ rawHtml }}</p>
        <p>Using v-html directive: <span v-html="rawHtml"></span></p>
    </div>

</template>
