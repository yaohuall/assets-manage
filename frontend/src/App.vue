<template>

    <el-container class="layout">
      <el-aside class='aside' width="auto">
          <Menu></Menu>
      </el-aside>
      <el-container>
        <el-header class="header">
            <Header></Header>
        </el-header>
        <el-main class="main">
            
            <router-view />
        </el-main>
        
      </el-container>

      
    </el-container>

</template>

<script lang="ts" setup>
import Header from './layout/Header.vue'
import Menu from './layout/Menu.vue'
import { useStore } from "vuex"
import axios from 'axios';

 const store = useStore()
 const loginStatus = () => {
     store.commit("initializeStore")
     const token = store.state.token
     if ( token ){
         axios.defaults.headers.common["Authorization"] = "Token "+ token
     }else{
         axios.defaults.headers.common["Authorization"] = ''
     }
     console.log('token initilized:' , axios.defaults.headers.common["Authorization"])
}

loginStatus()
</script>

<style scoped>
.layout{
    height: 100%;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.aside{
    background-color: #0d0d0e;
}

.header{
    height: 80px; /* same as logo height */
    border-bottom: 1px solid #e5e5e5; /* 邊框 */
    display: flex; /*使得物件從左往右放置*/
    align-items: center;
    justify-content: space-between;
    background-color: #2c2c38;
}

.main{
    background-color: #2c2c38;
}
</style>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
