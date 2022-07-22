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
import Header from './Header.vue'
import Menu from './Menu.vue'

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