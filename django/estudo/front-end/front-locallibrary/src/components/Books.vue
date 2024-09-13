<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import Pagination from "./Pagination.vue";
const url = ref("http://127.0.0.1:8000/api/v1/quickstart/books/");
const dataBooks = ref({ results: [] });

const erroApi = ref(false);
async function getBooks(pagina) {
    try {
        console.log(pagina);

        const books = await axios.get(pagina == "" ? url.value : pagina);

        dataBooks.value = books.data;
        console.log(dataBooks.value);
        
    } catch (e) {
        erroApi.value = true;
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
        <tbody v-bind:key="index" v-for="(item, index) in dataBooks.results">
            <tr class="table-info text-white">
                <td>
                    <a href="{{ `http://127.0.0.1:8000/api/v1/quickstart/books/${item.id}`}}">{{ item.title }}</a>
                </td>
                <td>{{ item.author_name }}</td>
                <td>{{ item.isbn }}</td>
            </tr>
        </tbody>
    </table>

    <div v-if="erroApi" class="alert alert-warning alert-dismissible" role="alert">
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
                <h4 class="alert-title">Wow! Everything worked!</h4>
                <div class="text-secondary">Your account has been saved!</div>
                <div class="btn-list">
                    <a @click="getBooks" href="#" class="btn btn-success">Try again</a>
                    >
                </div>
            </div>
        </div>
        <a class="btn-close" data-bs-dismiss="alert" aria-label="close"></a>
    </div>

    <div :style="{ height: '50px' }" v-if="dataBooks.results.length == 0 && erroApi == false"
        class="alert alert-important alert-danger alert-dismissible m-2 " role="alert">
        <div class="d-flex">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24"
                    viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                    stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <circle cx="12" cy="12" r="9"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
            </div>
            <div>There are no books</div>
        </div>
        
    </div>

   
    
    <div class="d-flex justify-content-center">
        <a v-if="dataBooks.previous != null" @click.prevent="() => {
            getBooks(dataBooks.previous);
        }
            " href="#">previous</a>
        <a v-if="dataBooks.next != null" @click.prevent="() => {
            getBooks(dataBooks.next);
        }
            " href="#">next</a>
    </div>

    <Pagination :next="dataBooks.next" :previous="dataBooks.previous"  :count="dataBooks.count"/>
</template>