import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Books from '@/components/Books.vue'
import BookDetail from '@/components/BookDetail.vue'
import AddNewBook from '@/components/AddNewBook.vue'
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
      component: AddNewBook,
    },
    {
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetail, 
      props: true 
    },

  ]
})

export default router
