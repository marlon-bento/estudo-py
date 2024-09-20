<script setup>
import { onMounted, ref } from 'vue';
import axios from "axios";
import AlertWarmingTryAgain from '@/components/AlertWarmingTryAgain.vue';
import Alert404 from '@/components/Alert404.vue';
//id passado pela rota
const props = defineProps(['id'])
const id = props.id

const url = ref(`http://127.0.0.1:8000/api/v1/quickstart/books/${id}/`)
const bookData = ref("")


const erroApi = ref("")

async function getBook() {
    try {
        erroApi.value = ""
        const book = await axios.get(url.value);
        bookData.value = book.data;
    } catch (e) {
        if (e.response && e.response.status === 404) {
            erroApi.value = "404"
        } else {
            erroApi.value = "error";
        }
    }
}
onMounted(async () => {
    await getBook()
})

</script>
<template>
    <div v-if="bookData" class="">
        <h1 class="display-3">Title: {{ bookData.title }}</h1>

        <p><strong>Author:</strong> <a href="#">{{ bookData.author_name }}</a></p>
        <!-- author detail link not yet defined -->
        <p class="lead">{{ bookData.summary }}</p>
        <div  style="margin-left:20px;margin-top:20px">
            <h4>Copies</h4>

            <div v-if="bookData.instances">
                <div :key="index" v-for="(item, index ) in bookData.instances">
                    <hr>
                    <p :class="item.status == 'a' ? 'text-success' :item.status =='m'? 'text-danger': 'text-warning'" ><strong>{{ item.status}}</strong></p>
                    <div v-if="item.status != 'a'" >
                        <p><strong>Due to be returned by {{item.borrower}} :</strong> {{item.due_back}}</p>
                    </div>

                    <p><strong>Imprint:</strong> {{item.imprint}}</p>
                    <p class="text-muted"><strong>Id:</strong> {{item.id}}</p>
                </div>
            </div>
            <div v-else>
                Este livro não possui instancias
            </div>
           


            
        </div>

    </div>
    <Alert404  description="Não há livros com esse id"   v-else-if="erroApi == '404'"  ></Alert404>
    
    <AlertWarmingTryAgain v-else title="Falha ao acessar o servidor"
    description="Por favor tente mais tarde" button="Tentar de novo" @try-again="getBook"></AlertWarmingTryAgain>
</template>
<style scoped></style>