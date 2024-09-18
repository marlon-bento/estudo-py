
<template>
    
    <form @submit.prevent="login" class="d-flex justify-content-center flex-column align-items-center gap-3">
        <h1>Log in</h1>

        <div class="">
            <label class="form-label">Username</label>
            <input v-model="username_input" type="text" class="form-control" name="example-text-input" placeholder="type your username" />
        </div>
        <div class="">
            <label class="form-label">Password</label>
            <input v-model="password_input" type="password" class="form-control" name="example-text-input" placeholder="type your password" />
        </div>

        <input class="btn btn-info" type="submit" value="Login">
        <p v-if="alert" class="text-danger">Preencha os 2 campos</p>
    </form>    
</template>
<script setup>
import axios from 'axios'
import { ref } from 'vue'

const user = ref('')
const username_input = ref('')
const password_input = ref('')
const alert = ref(false) 
function reloadPage(){
    window.location.reload()
}
async function login(){
    if(username_input.value && password_input.value){
        alert.value = false

        const dataObject={
            username: username_input.value,
            password: password_input.value
        }
        console.log(dataObject)
        try{
            const response = await axios.post('http://127.0.0.1:8000/api/v1/quickstart/token/', dataObject)
            user.value = response.data
            localStorage.setItem("first_name", user.value.first_name);
            localStorage.setItem("token", user.value.access);
            localStorage.setItem("refresh", user.value.refresh);
            //reloadPage()

        }catch(e){
            console.log(e)
        }
       
    }else{
        alert.value = true
    }

    
}

</script>