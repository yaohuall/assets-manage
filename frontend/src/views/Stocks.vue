<template>
    <div class="first">
        <!-- <el-row :gutter="12" style="margin-right:10px"> -->
            <el-col :span="16">
                <el-card shadow="hover">

                </el-card>
            </el-col>
            <el-col :span="8">
                <el-card shadow="hover">
                    {{  Data.NVDA }}
                </el-card>
            </el-col>
        <!-- </el-row> -->

        <!-- <el-row style="width:50%">
            <el-card class="charts" shadow="hover">


            </el-card>    
        </el-row> -->
    </div>

    <!-- <div class="second">
        <el-row :gutter="12">
            <el-col :span="16">
                <el-card shadow="hover">

                </el-card>
            </el-col> 

            <el-col :span="8">
                <el-card shadow="hover">
                </el-card>
            </el-col> 
        </el-row>
    </div> -->

</template>

<script lang="ts" setup>
import { ref, reactive, getCurrentInstance, watch, onMounted } from 'vue'

const API = (getCurrentInstance() as any).proxy.api
let Data = reactive({
    NVDA: ref('')
})

let getStocks = () =>{
    API.stocks.getData().then((res:any) => {
        console.log(res.data)
        Data.NVDA = res.data.data
    })
    .catch((error:any) => {
        console.log(error)
    })
}

getStocks()
</script>

<style scoped>
.first{
    height:100%;
    margin-bottom: 1%;
    display:flex;

}
.first .el-col{
    margin-right:5px
}
.second{
    height: 58%;
}
.second .el-row{
    height: 100%;
}
.el-card{
    height: 100%;
    background-color:black;
    --el-card-border-radius:10px;
    color: #00ff00;
    /* margin-bottom:30px;
    margin-top:5px */
}
.el-card:hover{
    margin-top: -5px;
}

</style>