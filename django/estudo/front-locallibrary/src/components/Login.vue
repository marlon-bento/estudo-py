
<template>
    <form v-if="!login.token" @submit.prevent="loginMetod" class="d-flex justify-content-center flex-column align-items-center gap-3">
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
    <div class="alert alert-success m-0" v-else>
        Você já está logado — <a href="#" @click.prevent="login.logoutAction" class="alert-link">logar com outra conta</a>!
    </div>
</template>
<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useLoginStore } from '@/stores/LoginStore.js';
const login = useLoginStore()

const user = ref('')
const username_input = ref('')
const password_input = ref('')
const alert = ref(false) 

async function loginMetod(){
    if(username_input.value && password_input.value){
        alert.value = false

        const dataObject={
            username: username_input.value,
            password: password_input.value
        }
        console.log(dataObject)
        try{
            await login.loginAction(dataObject)
        }catch(e){
            window.alert(e)
        }
       
    }else{
        alert.value = true
    }

    
}

</script>