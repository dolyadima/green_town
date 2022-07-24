import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/list_trees',
      name: 'list_trees',
      component: () => import('../views/ListTreesView.vue')
    },
    {
      path: '/tree_detail/:id',
      name: 'tree_detail',
      component: () => import('../views/DetailTreeView.vue')
    },
    {
      path: '/filter_trees',
      name: 'filter_trees',
      component: () => import('../views/FilterTreesView.vue')
    },
  ]
})

export default router
