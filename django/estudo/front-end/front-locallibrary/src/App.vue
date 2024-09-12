<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <main class="row">
    <div class="col-2 bg-info fixed-top h-100">
      <Header/>
    </div>
    <div class="offset-2 col-10 bg-dark ">
      <RouterView />
    </div>
  </main>

  
</template>

<style scoped>
  main{
    height: 100vh;
  }
</style>
