import './assets/main.css'

// Importar o CSS do Tabler
import '@tabler/core/dist/css/tabler.min.css';
// Importar o JavaScript do Tabler
import '@tabler/core/dist/js/tabler.min.js';

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia'

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(router)

app.mount('#app')
