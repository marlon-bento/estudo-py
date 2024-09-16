<script setup>
import { onMounted, ref } from "vue";

import AlertWarmingTryAgain from '@/components/AlertWarmingTryAgain.vue';
import Alert404 from '@/components/Alert404.vue';

import axios from "axios";
import Pagination from "./Pagination.vue";

const url = ref("http://127.0.0.1:8000/api/v1/quickstart/books/");
const dataBooks = ref({ results: [] });

const erroApi = ref("");
import { computed } from 'vue';
let currentPage  = computed(() => dataBooks.value.previous == null ? 1: dataBooks.value.previous+1);

async function getBooks(pagina) {
    try {
        erroApi.value = ""
        const books = await axios.get(pagina == "" ? url.value : pagina);
        dataBooks.value = books.data;

    } catch (e) {
        if (e.response && e.response.status === 404) {
            erroApi.value = "404"
        } else {
            erroApi.value = "error";
        }
    }
}

onMounted(async () => { 
   await getBooks("")
});
</script>


<template>
    <table v-if="dataBooks.results.length > 0" class="table">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">author</th>
                <th scope="col">ISBN</th>
            </tr>
        </thead>
        <tbody :key="index" v-for="(item, index) in dataBooks.results">
            <tr class="table-info text-white">
                <td>
                    <router-link :to="{ name: 'book-detail', params: { id: item.id } }">{{ item.title }}</router-link>  
                </td>
                <td>{{ item.author_name }}</td>
                <td>{{ item.isbn }}</td>
            </tr>
        </tbody>
    </table>

    <Alert404  description="Não há nenhum livro"   v-else-if="erroApi == '404'"  ></Alert404>
    
    <AlertWarmingTryAgain v-else title="Falha ao acessar o servidor"
    description="Por favor tente mais tarde" button="Tentar de novo" @try-again="getBooks"></AlertWarmingTryAgain>

    <Pagination :next="dataBooks.next" 
    :previous="dataBooks.previous"  
    :count="dataBooks.count" 
    :current="currentPage" 
    :total_pages="dataBooks.total_pages" 
    @previous-page="() => {getBooks(`${url}?page=${dataBooks.previous}`)}" 
    @change-page="(page) => {getBooks(`${url}?page=${page}`)}" 
    @next-page="() => {getBooks(`${url}?page=${dataBooks.next}`)}" />

</template>