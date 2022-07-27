import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../src/components/Home.vue'
import Login from '../src/components/Login.vue'
import SignUp from '../src/components/SignUp.vue'
import store from '../store'

const routes : Array<RouteRecordRaw> = [
    {
        path: "/home",
        component: Home,
        meta: {
            title: 'Home',
            requireLogin: true
        },
    },
    {
        path: "/login",
        component: Login,
        meta: {
            title: 'Login',
        },
    },
    {
        path: "/sign-up",
        component: SignUp,
        meta: {
            title: 'SignUp',
        },
    },

    // {
    //     path: '/per-info',
    //     component: Layout,
    //     name: 'per-info',
    //     children: [
    //         {
    //             path: '/per-info/manage',
    //             component: () => import('../src/components/PerManage.vue'),
    //             meta: {
    //                 title: 'Personal Information',
    //             },
    //         },
            
    //     ]
    // }

]

const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
)

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
      next('/login')
    }else{
      next()
    }
    if (to.path === '/') next('/home')
    else{
        next()
    }
  })
export default router