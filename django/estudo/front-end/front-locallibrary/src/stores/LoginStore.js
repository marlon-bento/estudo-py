import {defineStore} from 'pinia'
import axios from 'axios'
export const useLoginStore = defineStore('login', {
    //propriedades reativas
    state(){
        return{
            first_name: '',
            token: '',
            refresh:'',
        }
    },
    // metodos
    actions:{
        loginVerific(){
            console.log('verificando login')
            this.first_name= localStorage.getItem('first_name') || ''
            this.token = localStorage.getItem('token') || ''
            this.refresh = localStorage.getItem('refresh')|| ''
        },
        async verifyToken(){
            try {
                console.log("verificando token")
                const response = await axios.post('http://127.0.0.1:8000/api/v1/quickstart/token/verify/', {
                    token: this.token
                })
            } catch (e) {
                if(e.response.status == '401'){
                    console.error("Token expirado", e)
                    throw new Error('Seu ascesso está expirado, faça login novamente')
                }
                throw new Error('ERRO NO SERVIDOR OU FALHA NA RESPOSTA')
            }
        },
        async refreshToken(){
            try {
                console.log("refresh do token")
                const response = await axios.post('http://127.0.0.1:8000/api/v1/quickstart/token/refresh/', {
                    refresh: this.refresh
                })
                this.token = response.data.access
                localStorage.setItem('token', this.token)
                return this.token
            } catch (e) {
                console.error("Erro ao atualizar token", e)
                throw new Error('Falha ao atualizar o token')
            }

        },
        async loginAction(user){
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/v1/quickstart/token/', user)
                this.token = response.data.access
                this.refresh = response.data.refresh
                this.first_name = response.data.first_name
                localStorage.setItem('first_name', this.first_name)
                localStorage.setItem('token', this.token)
                localStorage.setItem('refresh', this.refresh)
            } catch (e) {
                console.error("Erro ao fazer login", e)
                throw new Error('Falha ao fazer login')
            }
        },
        logoutAction(){
            console.log("fiz logout")
            this.token = ''
            this.first_name = ''
            this.refresh = ''
            localStorage.removeItem('first_name') 
            localStorage.removeItem('token') 
            localStorage.removeItem('refresh') 
        }
    },
    // getters
    getters:{
        showLogin(){
            return this.first_name
        }
    }
})