<template>
    <div class="logo">
        <!-- <img src="../assets/icon-1.jpg" alt="logo"> -->
        <span class="title">Financial Info Dashboard</span>
    </div>
</template>

<script lang="ts" setup>
</script>

<style scoped>

.logo{
    background-color: rgb(7, 7, 7);
    height: 79px;
    border: none;
    display: flex;
    line-height: 50px;
    align-items: center;
    padding-left: 50px;
    color:	#00ff00;
    border-bottom: 1px solid #e5e5e5; /* 邊框 */
}

/* .logo img{
    height: 50px;
    width: 50px;
    margin-right: 12px;
} */

.logo span{
    display: flex;
    justify-content: center;
    font-weight: 600;
    line-height: 50px;
    font-size: 18px;
    vertical-align: middle;
}
</style>