<template>
    <!-- 不能使用div -->
    <el-container class="header-left">
        <!-- style size 需要添加在el-icon tag -->
        <!-- <el-icon style="margin-right: 50px;" :size="30">
            <component :is="isCollapse? Expand : Fold" @click="changeCollapse">
            </component>
        </el-icon> -->
        <div v-if="!isCollapse" @click="changeCollapse">
            <el-icon style="margin-right: 50px;" :size="30" >
                        <Fold />
            </el-icon>
        </div>
        <div v-else @click="changeCollapse">
            <el-icon style="margin-right: 50px;" :size="30" >
                        <Expand />
            </el-icon>
        </div>
        <el-breadcrumb separator="/">
            <!-- <el-breadcrumb-item>Home</el-breadcrumb-item> -->
            <el-breadcrumb-item v-for="item in tabs">{{ item.meta.title }}</el-breadcrumb-item>
            <!-- <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
            <el-breadcrumb-item>promotion list</el-breadcrumb-item>
            <el-breadcrumb-item>promotion detail</el-breadcrumb-item> -->
        </el-breadcrumb>
    </el-container>
    <div>

        <span class="user-info" v-if="store.state.isAuthenticated">
            Hi! {{ userInfo.username }}
        </span>
    </div>
    <!-- <el-dropdown>
        <span class="el-dropdown-link" >
        User
            <el-icon class="el-icon--right">
                <arrow-down />
            </el-icon>
        </span>
        <template #dropdown>
            <el-dropdown-menu class="drop">
                <el-dropdown-item>Action 1</el-dropdown-item>
                <el-dropdown-item>Action 2</el-dropdown-item>
                <el-dropdown-item>Action 3</el-dropdown-item>
            </el-dropdown-menu>
        </template>
    </el-dropdown> -->
</template>

<script lang="ts" setup>
import { Ref, ref, computed, watch, getCurrentInstance } from "vue"
import { useStore } from "vuex"
import { Fold, Expand } from "@element-plus/icons-vue";
import { useRoute, RouteLocationMatched} from "vue-router";
import axios from "axios";

const tabs: Ref<RouteLocationMatched[]> = ref([])
const route = useRoute()
const API = (getCurrentInstance() as any).proxy.api

const getBredCum = () => {
    let matched = route.matched.filter(item=>item.meta && item.meta.title)
    tabs.value = matched
}
const store = useStore()
const localCollapse = ref(false)
const localUser = ref('')
const isCollapse = computed(()=>{
    localCollapse.value = store.getters['getCollapse']
    return store.getters['getCollapse']
})

const changeCollapse = () => {
    // console.log('changed..')
    localCollapse.value = !localCollapse.value
    store.commit('setCollapse', localCollapse.value)
}

const userInfo = computed(()=>{
    localUser.value = store.getters['getUserinfo']
    return store.getters['getUserinfo']
})
// const getUser = () =>{
//     API.user.getData().then(res =>{
//         console.log(res)
//         if (res.data !== undefined) {
//         // user = res.data.username
//         let userInfo = ''
//         }else{
//            let userInfo = ''
//         }
//     }).catch(error => {
//         console.log(error)
//     })
// }
// getUser()
getBredCum()

watch(() => route.path, ()=>getBredCum())
</script>

<style scoped>
.el-container header-left{
    display: flex;
    align-items: center;
}


.el-dropdown {
    font-size:30px;
    color: #00ff00
}
:deep(.el-breadcrumb .el-breadcrumb__inner) {
        color: #00ff00;
        font-size: 30px;
        /* background-color: black; */
}

:deep(.el-breadcrumb__item:last-child .el-breadcrumb__inner, .el-breadcrumb__item:last-child .el-breadcrumb__inner a, .el-breadcrumb__item:last-child .el-breadcrumb__inner a:hover, .el-breadcrumb__item:last-child .el-breadcrumb__inner:hover) {
        color: #00ff00;
        font-size: 30px;
        /* background-color: black; */
}
.el-dropdown-menu{
    padding: 0px;
    margin: 0px;
    border-top: 0px;
    /* 可以在瀏覽器查看屬性 */
    --el-dropdown-menuItem-hover-fill: #00ff00;
    --el-dropdown-menuItem-hover-color: black
}

/* .el-dropdown-menu-item.is-active{
    color:#00ff00 !important
} */
.el-icon{
    color:#00ff00
}
</style>

<style>
/* 修改dropdwon menu style 不能使用scoped */
.drop li{
    color: 	#00ff00;
    background-color: #2c2c38;
    font-size: 25px;
    padding: 15px;
    margin: 0px;
}
.user-info{
    color:#00ff00
}
</style>