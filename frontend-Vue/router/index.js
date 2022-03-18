import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Nav',
        component: () => import('../views/Nav.vue'),
        children: [
            {
                path: '/home',
                name: 'home',
                component: () => import('../views/home')
            },
            {
                path: '/user',
                name: 'user',
                component: () => import('../views/User')
            },
            {
                path: '/char',
                name: 'char',
                component: () => import('../views/char')
            },
            {
                path: '/item',
                name: 'item',
                component: () => import('../views/item')
            },
            {
                path: '/mons',
                name: 'mons',
                component: () => import('../views/mons')
            },
            {
                path: '/weap',
                name: 'weap',
                component: () => import('../views/weap')
            },
            {
                path: '/more',
                name: 'more',
                component: () => import('../views/more')
            }
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: () => import ('../views/Login/login.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router