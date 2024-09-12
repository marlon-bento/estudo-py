<script setup>
import { onMounted, ref } from 'vue';
import axios from "axios"
const url = ref("http://127.0.0.1:8000/api/v1/quickstart/books/")
const dataBooks = ref({data:[]})
async function getBooks(pagina) {
    try {
        console.log(pagina)
        
        const books = await axios.get(pagina == "" ? url.value : pagina)

        dataBooks.value = books.data;
        console.log(typeof(dataBooks.value.next))
    } catch (e) {
        alert("deu erro ai tiu")
    }

}

onMounted(async () => {
    await getBooks("");
});
</script>


<template>
    <table class="table ">
        <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">author</th>
            <th scope="col">ISBN</th>
        </tr>
        </thead>
        <tbody    v-bind:key="index" v-for="(item, index) in dataBooks.results" >
   
            <tr class="table-info text-white" >
                <td><a href="{{ `http://127.0.0.1:8000/api/v1/quickstart/books/${item.id}`}}">{{ item.title }}</a></td>
                <td>{{item.author_name}}</td>
                <td>{{item.isbn}}</td>
            </tr>
        </tbody>
    </table>
    <div class="d-flex justify-content-center">
    
        <a v-if="dataBooks.previous != null" @click.prevent="() => {getBooks(dataBooks.previous)}" href="#">previous</a>
        <a v-if="dataBooks.next != null" @click.prevent="() => {getBooks(dataBooks.next)}" href="#">next</a>
    </div>


   
</template>