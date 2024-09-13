<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <main class="row">
    <div class="col-2 bg-dark fixed-top h-100">
      <Header/>
    </div>
    <div class="offset-2 col-10 bg-white  h-100  p-3">
      <RouterView />
    </div>
  </main>

  
</template>

<style scoped>
  main{
    height: 100vh;
  }
</style>
