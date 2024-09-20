<script setup>

const props = defineProps(['next', 'previous', 'count', 'current', 'total_pages'])
const emit = defineEmits(['nextPage', 'previousPage', 'changePage']);
</script>
<template>

   <div class="d-flex gap-2 align-items-center justify-content-center">

      <a @click.prevent="$emit('previousPage')" v-if="props.previous" class="svg-back" href="#">
         <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000"
            stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
            class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-left">
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path d="M15 6l-6 6l6 6" />
         </svg>
      </a>

      <div v-for="n in props.total_pages" :key="n" >
         <div v-if="props.total_pages < 100">
            <div>
               <a @click.prevent="$emit('changePage', n)"
                  class="field-input-page d-flex justify-content-center align-items-center "
                  :class="props.current == n ? 'bg-dark' : 'bg-gray-900'" href="#">
                  <div>
                     {{ n }}
                  </div>
               </a>
            </div>
         </div>
         <div v-else>

         </div>

      </div>


      <a @click.prevent="$emit('nextPage')" v-if="props.next" class="svg-next" href="#">
         <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000"
            stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
            class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-right">
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path d="M9 6l6 6l-6 6" />
         </svg>
      </a>

   </div>



</template>
<style scoped>

.field-input-page{
  min-width: 30px;
  min-height: 30px;
}

</style>