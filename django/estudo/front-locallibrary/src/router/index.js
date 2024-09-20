import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Books from '@/components/Books.vue'
import BookDetail from '@/components/BookDetail.vue'
import AddNewBook from '@/components/AddNewBook.vue'
import BookPut from '@/components/BookPut.vue'
import Login from '@/components/Login.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    },
    {
      path: '/add/book',
      name: 'add-book',
      beforeEnter: function (to, from, next) {
        const token = localStorage.getItem('token')

        if (!token) {
          next('/login')
        } else {
          next()
        }
      },
      component: AddNewBook,
    },
    {
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetail, 
      props: true 
    },
    {
      path: '/books/put/:id',
      name: 'book-put',
      component: BookPut, 
      props: true 
    },
    {
      path: '/login',
      name: 'login',
      component: Login, 
    },

  ]
})

export default router
