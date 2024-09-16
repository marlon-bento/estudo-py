<script setup>
import axios from 'axios';
import {onMounted, ref} from 'vue'

const dataAuthors = ref([])
const genresData = ref([])
async function getAuthors(){
    try{
        const authors = await axios.get("http://127.0.0.1:8000/api/v1/quickstart/all/authors/")
        dataAuthors.value = authors.data
        
    }catch(e){
        console.log(e)
    }
}

async function getGenres(){
    try{
        const genres = await axios.get("http://127.0.0.1:8000/api/v1/quickstart/all/genres/")
        dataGenres.value = genres.data
        
    }catch(e){
        console.log(e)
    }
}

onMounted(async ()=>{
    
    await getAuthors()
    await getGenres()
})
</script>

<template>
    <form>

        <div class="mb-3">
            <label for="inputAuthors" class="form-label">Select</label>
            <select class="form-select" id="inputAuthors" name="cars" aria-label="Floating label select example" >
                <option :key="index" v-for="(item, index) in dataAuthors" :value="item.id">{{item.first_name + " " + item.last_name}}</option>
            </select> 
        </div>


        
        
        


    </form>
    
</template>

<style scoped>


</style>