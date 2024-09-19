<script setup>
import { onMounted, ref } from "vue";

import AlertWarmingTryAgain from '@/components/AlertWarmingTryAgain.vue';
import Alert404 from '@/components/Alert404.vue';

import axios from "axios";
import Pagination from "./Pagination.vue";
import Confirm from "./Confirm.vue";

import { useLoginStore } from "@/stores/LoginStore";
import { computed } from 'vue';

const url = ref("http://127.0.0.1:8000/api/v1/quickstart/books/");
const dataBooks = ref({ results: [] });
const confirmComponent = ref(false);
const verificationVar = ref("")
const filhoRef = ref(null)
const erroApi = ref("");
const bookId = ref("")
const login = useLoginStore()



let currentPage = computed(() => dataBooks.value.previous == null ? 1 : dataBooks.value.previous + 1);

async function getBooks(pagina) {
    try {
        erroApi.value = ""
        const books = await axios.get(pagina == "" ? url.value : pagina);
        dataBooks.value = books.data;

    } catch (e) {
        if (e.response && e.response.status === 404) {
            erroApi.value = "404"
        }else if (e.response && e.response.status === 401) {
            erroApi.value = "401"
        }
        else {
            erroApi.value = "error";
        }
    }
}
async function functionDeleteBook(id){
    try {
        const response = await axios.delete(`${url.value}${id}/`, {
            headers: {
                'Authorization': `Bearer ${login.token}`
            }
        });
        return response;
    } catch (e) {
        throw e;
    }
}
async function deleteBook(id) {
    confirmComponent.value = false
    if(login.token){
        try {
            await functionDeleteBook(id)
            alert("Livro deletado com sucesso");
            await getBooks(""); // Atualiza a lista de livros após a exclusão
        } catch (e) {
            if (e.response && e.response.status === 404) {
                erroApi.value = "404"
            }
            else if (e.response && e.response.status === 401) {
                //neste caso tenta fazer refresh no token
                try {
                    await login.refreshToken();
                    await functionDeleteBook(id);
                    alert("Livro deletado com sucesso");
                    await getBooks(""); 
                } catch (refreshError) {
                    try{
                        await login.verifyToken()
                        erroApi.value = "401";
                    }catch (verifyError) {
                        login.logoutAction()
                        alert(verifyError.message);
                    }
                    
                }
            } else {
                erroApi.value = "error";
            }
        }
    }else{
        window.alert('para deletar um livro primeiro faça login')
    }


}

onMounted(async () => {
    await getBooks("")
});
</script>


<template>
    <Alert404 description="Sem permissão ou não está logado" v-if="erroApi == '401'"></Alert404>
    <Confirm ref="filhoRef" v-if="confirmComponent" @yes="() => { deleteBook(bookId) }" @no="confirmComponent = false">
    </Confirm>
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

                <td class="d-flex gap-3">
                    <router-link class="btn btn-info"
                        :to="{ name: 'book-put', params: { id: item.id } }">Edit</router-link>
                    <button @click="() => { bookId = item.id; confirmComponent = true }" class="btn btn-danger">Del</button>
                </td>

            </tr>
        </tbody>
    </table>

    <Alert404 description="Não há nenhum livro" v-else-if="erroApi == '404'"></Alert404>
    

    <AlertWarmingTryAgain v-else title="Falha ao acessar o servidor" description="Por favor tente mais tarde"
        button="Tentar de novo" @try-again="getBooks"></AlertWarmingTryAgain>

    <Pagination :next="dataBooks.next" :previous="dataBooks.previous" :count="dataBooks.count" :current="currentPage"
        :total_pages="dataBooks.total_pages" @previous-page="() => { getBooks(`${url}?page=${dataBooks.previous}`) }"
        @change-page="(page) => { getBooks(`${url}?page=${page}`) }"
        @next-page="() => { getBooks(`${url}?page=${dataBooks.next}`) }" />

</template>