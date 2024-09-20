<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue'
import AlertScuccess from '@/components/AlertScuccess.vue'
import { useLoginStore } from '@/stores/LoginStore';
const dataAuthors = ref([])
const dataGenres = ref([])
const login = useLoginStore()

// variaveis dos formularios

const checkedGenres = ref([])
const title = ref("")
const summary = ref("")
const author = ref("")
const isbn = ref("")
const create = ref("")


const alert = ref(false) 

async function enviarDados(){
    if(checkedGenres.value.length > 0 && title.value && summary.value && author.value && isbn.value){
        alert.value = false

        const dataObject={
            title : title.value,
            genre: checkedGenres.value,
            summary: summary.value,
            isbn: isbn.value,
            author: author.value
        }
        try{
            const response = await axios.post("http://127.0.0.1:8000/api/v1/quickstart/books/",dataObject,    {headers: {
                'Authorization': `Bearer ${login.token}`
            }})

            console.log(response.data) 
            create.value = response.data


        }catch(e){
            console.log(e)
        }
       
    }else{
        alert.value = true
    }
}
function createNew(){
    checkedGenres.value = []
    title.value = ""
    summary.value = ""
    author.value = ""
    isbn.value = ""

    create.value = ""
}

async function getAuthors() {
    try {
        const authors = await axios.get("http://127.0.0.1:8000/api/v1/quickstart/all/authors/")
        dataAuthors.value = authors.data

    } catch (e) {
        console.log(e)
    }
}

async function getGenres() {
    try {
        const genres = await axios.get("http://127.0.0.1:8000/api/v1/quickstart/all/genres/")
        dataGenres.value = genres.data
        console.log(dataGenres.value)
    } catch (e) {
        console.log(e)
    }
}

onMounted(async () => {

    await getAuthors()
    await getGenres()
})
</script>

<template>
    <AlertScuccess  v-if="create" button="Add More" title="Livro criado com sucesso" :description="'o livro '+create.title+' foi criado com sucesso'"  @more="createNew"></AlertScuccess>
    <form class="bg-cyan-lt rounded  p-6" v-else>
        <h1 class="text-center">Adicionar novo livro</h1>

        <div class="row mb-3">
            <div class="col-6">
                <label class="form-label">Title</label>
                <input v-model="title" type="text" class="form-control" name="example-text-input" placeholder="Input placeholder" />
            </div>
            <div class="col-6">
                <label class="form-label">ISBN</label>
                <input v-model="isbn" type="text" class="form-control" name="example-password-input" placeholder="Input placeholder" />
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label">Summary</label>
            <textarea v-model="summary" class="form-control" name="example-textarea" placeholder="Textarea placeholder"></textarea>
        </div>


        <div class="mb-3">
            <label for="inputAuthors" class="form-label">Author</label>
            <select v-model="author" class="form-select" id="inputAuthors" name="inputAuthors"
                aria-label="Floating label select example">
                <option :key="index" v-for="(item, index) in dataAuthors" :value="item.id">{{ item.first_name + " " +
                    item.last_name }}</option>
            </select>
        </div>







        <div class=" p-3">
            <div class="form-label">Escolha os generos</div>
            <div class="row gap-4 justify-content-center">
                <label :key="index" v-for="(item, index) in dataGenres" class="form-check col-3">
                    <input v-model="checkedGenres" :value="item.id" class="form-check-input border border-dark border-opacity-50" type="checkbox">
                    <span  class="form-check-label">{{ item.name }}</span>
                </label>
            </div>
        </div>
        
        <div class="d-flex justify-content-center">
            <input @click.prevent="enviarDados" type="submit" class="btn btn-success" value="Enviar">
        </div>
        <p v-if="alert" class="text-danger text-center">Por favor envie todos os dados</p>


    </form>

</template>

<style scoped></style>