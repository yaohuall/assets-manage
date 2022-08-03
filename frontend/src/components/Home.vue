<template>
    <div class="first">
        <el-row :gutter="12" style="margin-right:10px">
            <el-col :span="24">
                <el-card shadow="hover">
                    <div class="exchange" style="height: 50px">
                        <el-input v-model="numbers" placeholder="Input the amount" />
                        <el-select poper-class="cur" v-model="Data.rate" clearable placeholder="Select">
                                <el-option
                                v-for="item in Data.rateOptions"
                                :key="item.id"
                                :label="item.name"
                                :value="item.id"
                                />
                        </el-select>
                            <el-button type="primary" :icon="DArrowRight" @click="changeTWD()"></el-button>
                            <el-input disabled v-model="Data.result" />
                            <el-button class="clean-input" type="primary" @click="getChartData()">Clean</el-button>
                    </div>
                    <el-table :data="Data.currencies" style="margin-top:0px">
                        <el-table-column prop="CURRENCY" align="center" label="Currency"/>
                        <el-table-column prop="RATE" align="center" label="TWD"  />
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

        <el-row style="width:50%">
            <el-card class="charts" shadow="hover">


                <div ref="chartRef" style="width:110%; height:250%"></div>
            </el-card>    
        </el-row>
    </div>

    <div class="second">
        <el-row :gutter="12">
            <el-col :span="16">
                <el-card shadow="hover">
                    <div class="asset">
                        <el-button class="table-button" type="primary" style="height:50px" :icon="Plus" @click="addAsset()">Add asset</el-button>
                        <el-button class="table-button" type="primary" style="height:50px" :icon="Edit" @click="calAsset()">Assets value</el-button>
                        <el-button class="table-button" type="primary" style="height:50px" :icon="Edit" @click="cancelAmount()">Clean amount</el-button>
                        <p class="amount">Total amount: {{ Data.totalAmount }}</p>
                    </div> 
                    <el-table :data="Data.assets" style="margin-top:0px" @selection-change="handleSelectionChange">
                        <el-table-column type="selection" width="55" />
                        <el-table-column width="150">
                            <template #default="scope">
                                <el-button class="table-button" type="primary" :icon="Delete" @click="delAsset(scope.row)" ></el-button>
                                <el-button class="table-button" type="primary" :icon="Edit" @click="editAsset()"></el-button>
                                <!-- <el-button class="table-button" type="primary" :icon="More"></el-button> -->
                            </template>
                        </el-table-column>
                        <el-table-column width="120" prop="asset_type" align="center" label="Asset type"/>
                        <el-table-column prop="name" align="center" label="Name"  />
                        <el-table-column prop="purchased_price" align="center" label="Purchased price"  />
                        <el-table-column prop="actual_price" align="center" label="Actual price"  />
                        <el-table-column prop="memo" align="center" label="Memo"  />
                        <el-table-column prop="date" align="center" label="Date"  />
                    </el-table>
                </el-card>
                <!-- <el-input v-model="query" placeholder="Search News" /> -->
            </el-col> 

            <el-col :span="8">
                <el-card shadow="hover">
                    <div ref="piechartRef" class="pie-chart" style="width:120%; height:300%"></div>
                </el-card>
            </el-col> 
        </el-row>
    </div>

    <div class="dialog-info">
        <el-dialog v-model="Data.dialogFormVisible" title="Add Asset" width="40%" @close="cancelAsset()">
            <el-form :model="Data.assetsForm" :rules="Data.rules" ref="ruleFormRef">
                <el-form-item label="Asset type" prop="asset_type">
                    <el-select v-model="Data.assetsForm.asset_type" placeholder="Please select">
                        <el-option  label="stock" value="stock" />
                        <el-option  label="salary" value="salary" />
                        <el-option  label="spend" value="spend" />
                        <el-option  label="pay" value="pay" />
                        <el-option  label="received" value="received" />
                    </el-select>
                </el-form-item>
                <el-form-item label="Asset name" >
                    <el-input style="width:50%" v-model="Data.assetsForm.name" placeholder="please input"/>
                </el-form-item>
                <el-form-item label="Purchased price" prop="purchased_price">
                    <el-input style="width:50%" v-model="Data.assetsForm.purchased_price" placeholder="please input"/>
                </el-form-item>
                <el-form-item label="Actual price" prop="actual_price">
                    <el-input style="width:50%" v-model="Data.assetsForm.actual_price" placeholder="please input"/>
                </el-form-item>
                <el-form-item label="Date" >
                    <el-date-picker v-model="Data.assetsForm.date" type="date" 
                    placeholder="Pick a day" value-format="YYYY-MM-DD"/>
                </el-form-item>
                <el-form-item label="Memo" prop="memo">
                    <el-input style="width:50%" v-model="Data.assetsForm.memo" placeholder="please input"/>
                </el-form-item>
            </el-form>
            <template #footer>
            <span class="dialog-footer">
                <el-button @click="cancelAsset()">Cancel</el-button>
                <el-button type="primary" @click="submitForm(ruleFormRef)"
                >Confirm</el-button
                >
            </span>
            </template>
        </el-dialog>
    </div>
</template>

<script lang="ts" setup>
import { ref, reactive, getCurrentInstance, watch, onMounted } from 'vue'
import { Search, DArrowRight, Plus, Remove, Delete, Edit, More } from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from "element-plus";
import * as echarts from 'echarts'
import { useStore } from "vuex"
import axios from 'axios'
const API = (getCurrentInstance() as any).proxy.api

const store = useStore()
let query = ref("")
let numbers = ref("")
let mycharts = ref()
let mypiecharts = ref()
// <HTMLElement>: 預告為html element
let chartRef = ref<HTMLElement>()
let piechartRef = ref<HTMLElement>()

const ruleFormRef = ref('')
const multipleSelection = ref([])
let Data = reactive({
    result: ref(0),
    exchangeRate: reactive({
        USD: ref(0),
        USDTWD: ref(0)
    }),
    totalAmount: ref(0),
    currencies: reactive([
    ]),
    assets: reactive([
    ]),
    assetsName: reactive([
    ]),
    assetsPrice: reactive([
    ]),
    rateOptions: reactive([
        {id:1, name:'TWD to USD'},
        {id:2, name:'TWD to CNY'},
    ]),
    assetsForm: reactive({
      asset_type:ref(""),
      name:ref(""),
      purchased_price:ref(null),
      actual_price:ref(null),
      date:ref(""),
      memo:ref("")
    }),
    dialogFormVisible: ref(false),
    rules: reactive({
        asset_type: [
                { required: true, message: "asset type can't be emptye", trigger: "blur" },
                // {
                //     pattern: /^[9][5]\d{4}$/,
                //     message: "",
                //     trigger: "blur",
                // },
                // {validator: validatesNoExists, trigger: 'blur' }
            ],
        purchased_price: [
                {
                    pattern: /^\d+$/,
                    message: "price needs to be integer!",
                    trigger: "blur",
                },
            ],
        actual_price: [
                {
                    pattern: /^\d+$/,
                    message: "price needs to be integer!",
                    trigger: "blur",
                },
            ],
    }),
})

let getRates = () => {
    API.rates.getData().then((res:any) => {
        Data.currencies = res.data
    })
    .catch((error:any) => {
        console.log(error)
    })
}

let getChartData = () => {
    API.rateChart.getData().then((res:any) => {
        console.log("yo")
        console.log(res.data)
        // Data.currencies = res.data
    })
    .catch((error:any) => {
        console.log(error)
    })
}

let changeTWD = () => {
    let ratetype = Data.rate
    const currate = Data.currencies[Number(ratetype)-1].RATE
    Data.result = Number(numbers.value) / Number(currate)
}

onMounted(() => {
        // as HTMLElement避免報錯
        getAssets()
        console.log(Data.assetsPrice)
        mycharts.value = echarts.init(chartRef.value as HTMLElement)
        mycharts.value.setOption({

                title: {
                    text: 'TWD to USD: One Year Exchange Rate',
                    textStyle: {
                        color: '#00ff00'
                    }
                },
                tooltip: {
                },
                xAxis: {
                    data: ['1', '2', '3', '4', '5', '6']
                },
                yAxis: {
                },
                series: [
                    {
                    name: 'ef',
                    type: 'line',
                    data: [5, 20, 36, 10, 10, 20],
                    itemStyle: {
                                normal: {
                                            color:"#00ff00"
                                        },
                                },
                    }
                ]
        })
    }
)

let getAssets = () =>{
    API.assets.getData().then((res:any) => {
        // console.log(res.data)
        Data.assets = res.data
        let assetsPrice = []
        let assetsName = []
         for (let i of res.data){
               assetsPrice.push({value:i.actual_price, name:i.asset_type})
               assetsName.push(i.asset_type)
        }
        // console.log(Data.assetsName)
        // console.log(Data.assetsPrice)
        mypiecharts.value = echarts.init(piechartRef.value as HTMLElement)
        mypiecharts.value.setOption(
            {
            title: {
                text: 'Assets distribution',
                // subtext: '纯属虚构',
                // x: 'center',
                textStyle: {
                        color: '#00ff00'
                    }
          },
          tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)",
          },
          legend: {
            data: assetsName,
            left:"center",                              
            top:"bottom",                              
            orient:"horizontal",     
            textStyle: {
                    color: '#00ff00'
                }                   
          },
          series: [
            {
              name: 'Asset value',
              type: 'pie',
            //   radius: ['10%', '70%'],
            //   center: ['10%', '10%'],
              data: assetsPrice,
              animationEasing: 'cubicInOut',
              animationDuration: 2600,
            }
          ]
            }
        )
    })
    .catch((error:any) => {
        console.log(error)
    })
}
let addAsset = () =>{
  Data.dialogFormVisible = true;
}

let cancelAsset = () => {
    Data.dialogFormVisible = false;
    Data.assetsForm.name = ref('')
    Data.assetsForm.purchased_price = ref(null)
    Data.assetsForm.actual_price = ref(null)
    Data.assetsForm.date = ref('')
    Data.assetsForm.asset_type = ref('')
    Data.assetsForm.memo = ref('')
}

let editAsset = () => {
    console.log("")
}

const delAsset = (row:any)=>{
  let confirmStr = "Are you sure to delete this asset record?";
  ElMessageBox.confirm(confirmStr).then(()=>{
    // 删除！
    API.assets.del(row.id).then((res)=>{
      if(res.status === 204){
            // 重新加载数据
              getAssets();
              // 提示添加成功！
              ElMessage({
                message:"Delete sucess!",
                type:'success'
              })
      }
    })
  })
}

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
            API.assets.addData(Data.assetsForm).then((res)=>{
            // 重新加载数据
            getAssets();
            // 关闭弹出层 
            cancelAsset();
            // 提示添加成功！
            ElMessage({
                message:"Add successfully!",
                type:'success'
            })
          })
    } else {
      console.log('error submit!', fields)
    }
  })
}

const handleSelectionChange = (val) => {
    multipleSelection.value = val
}

const calAsset = () =>{
    for (let i of multipleSelection.value){
        Data.totalAmount += i.actual_price
  }
}

const cancelAmount =() =>{
    Data.totalAmount = 0;
}

getRates()
getAssets()
getChartData()
</script>

<style scoped>
.first{
    height:40%;
    margin-bottom: 1%;
    display:flex;

}
.first .el-row{
    height: 100%;
    width: 50%
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

.first .el-input{
    --el-input-bg-color:black;
    --el-input-text-color: #00ff00;
    --el-input-focus-border-color: #00ff00;
    margin-bottom: 5px;
    --el-input-height:40px;
    width: 30%;
    margin-right: 10px;
    height: 43px
}

.first .el-button{
    /* margin-top: -2px; */
    width: 70px;
    height: 43px;
    font-size: 18px;
}
.exchange{
    display:flex;
}
.asset{
    display: flex;
}
.amount{
    margin-left: 10px;
    margin-left: auto;
    padding-top:10px
}

.first .el-select{
    --el-select-input-focus-border-color:#00ff00;
    width: 35%;
    margin-right: 10px
}
.first .el-select :deep(.el-input){
    --el-input-bg-color:black;
    --el-input-focus-border:#00ff00;
    --el-input-focus-border-color:#00ff00;
}
.first .el-select :deep(.el-input__inner){
    color:#00ff00;
    height:40px;
}
.first :deep(.el-input.is-disabled .el-input__wrapper){
    background-color:black;
}
.first :deep(.el-input.is-disabled .el-input__inner){
    color:#00ff00
}
.charts{
    width:100%
}

.el-table{
  font-size: 18px;
  --el-table-text-color: #00ff00;
  --el-table-header-text-color:#00ff00;
  --el-table-header-bg-color:black;
  /* --el-table-row-hover-bg-color:black; */
  --el-table-tr-bg-color:black;
  --el-table-row-hover-bg-color:rgba(163, 161, 128, 0.829);
  /* --el-table-current-row-bg-color:black; */
  --el-table-bg-color:black;
}

.el-button--primary {
    --el-button-text-color: #00ff00;
    --el-button-bg-color: black;
    --el-button-border-color: white;
    --el-button-hover-text-color: black;
    --el-button-hover-bg-color: #00ff00;
    --el-button-hover-border-color: white;
    margin-right:10px
}
.table-button{
    margin-right: 0px;
}
/* .el-select .el-input{
    --el-input-bg-color:black
} */

.el-select-dropdown__item.hover{
    background-color: rgba(163, 161, 128, 0.829);
}
.el-select-dropdown__item{
    color:#00ff00
}
:deep(.el-form-item__label){
    color:#00ff00
}
.dialog-info :deep(.el-dialog){
    --el-dialog-bg-color:rgb(0, 0, 0);
}

.dialog-info :deep(.el-dialog__title){
    color:#00ff00
}
.dialog-info :deep(.el-input__wrapper){
    background-color: black;
    --el-input-focus-border-color:#00ff00;
}
.dialog-info :deep(.el-input__inner){
    color:#00ff00;
}
.dialog-info :deep(.el-button){
    --el-button-text-color: #00ff00;
    --el-button-bg-color: black;
    --el-button-border-color: white;
    --el-button-hover-text-color: black;
    --el-button-hover-bg-color: #00ff00;
    --el-button-hover-border-color: white;
}
.dialog-info :deep(.el-select){
    --el-select-input-focus-border-color: #00ff00
}
.dialog-info :deep(.el-date-picker .el-in){
    --el-datepicker-active-color:#00ff00;
    --el-datepicker-hover-text-color:#00ff00;
    --el-datepicker-inrange-bg-color:#00ff00
}
:deep(.el-checkbox){
    --el-checkbox-checked-bg-color:black;
    --el-checkbox-checked-icon-color:#00ff00
}
:deep(.el-message-box__content){
    color:#00ff00
}
.pie-chart{
    margin-top:20px,
}
</style>

<style>
.el-select-dropdown {
       border: none;
       background-color: black
   }

.el-picker-panel{
    background:black;
    color:#00ff00
}
.el-popper.is-light{
    background:black
}
.el-date-picker{
    --el-datepicker-active-color:#00ff00;
    --el-datepicker-hover-text-color:#00ff00;
    --el-datepicker-inrange-bg-color:#00ff00;
    --el-datepicker-text-color:#00ff00;
    --el-datepicker-header-text-color:#00ff00;
    --el-datepicker-icon-color:#00ff00
}
.el-message-box{
    background-color:black;
}
.el-message-box__btns .el-button--primary{
    --el-button-bg-color:black;
    --el-button-text-color:#00ff00;
    --el-button-border-color:white;
    --el-button-hover-bg-color:#00ff00;
    --el-button-hover-text-color:black
}
.el-message-box__btns .el-button{
    --el-button-bg-color:black;
    --el-button-text-color:#00ff00;
    --el-button-border-color:white;
    --el-button-hover-bg-color:#00ff00;
    --el-button-hover-text-color:black
}
.el-message-box__content{
    color:#00ff00
}
</style>