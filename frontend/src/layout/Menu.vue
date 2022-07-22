<template>
    <MenuLogo v-if="!isCollapse" class="layout-logo"/>
 <el-menu
        active-text-color="#ffd04b"
        background-color="#0d0d0e"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="	#00ff00"
        :collapse="isCollapse"
        router
      >
        <el-menu-item index="/"><el-icon><HomeFilled /></el-icon></el-menu-item>

        <el-sub-menu index="1">
          <template #title>
            <el-icon><setting /></el-icon><span class="cate">Financial Info</span>
          </template>
            <el-menu-item index="/per-info/status">Status</el-menu-item>
            <el-menu-item index="/per-info/manage">Manage</el-menu-item>
        </el-sub-menu>
<!-- 
        <el-sub-menu index="2">
          <template #title>
            <el-icon><setting /></el-icon><span class="cate">Market Status</span>
          </template>
            <el-menu-item index="/home/student">Status</el-menu-item>
        </el-sub-menu> -->


      </el-menu>
</template>

<script lang="ts" setup>
import MenuLogo from './MenuLogo.vue'
import { ref, computed } from "vue"
import { useStore } from 'vuex'

// 綁定側邊欄的收縮 :collapse 為ture為收
// let isCollapse = ref(true);
const store = useStore()

const isCollapse = computed(() => {
    return store.getters['getCollapse']
})
</script>

<style scoped>
.cate{
  font-size:22px
}


.el-menu-item {
    display: block;
    text-align: center;
    font-size: 22px;
    --el-menu-hover-bg-color: rgba(163, 161, 128, 0.829);
    --el-menu-hover-text-color: #dae0da;

}

/* 如果导航的收起/展开动画无法正常展示，通常是由于导航整体的宽度未设置而引起。设置样式： */
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 300px;
  min-height: 400px;
}
/* 
解決el-menu 與 aside 邊框不一致問題 */
.el-menu {
  border-right: none;
}

@keyframes logoAnimation {
    0%{
        transform: scale(0);
    }
    50%{
        transform: scale(1);
    }
    100%{
        transform: scale(1);
    }
}

.layout-logo{
    animation: logoAnimation 1s ease-out;
}
</style>