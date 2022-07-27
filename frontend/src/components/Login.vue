<template>
    <div class="card">
        <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                label-width="200px"
                class="demo-ruleForm"
                status-icon
                style="width: 30%"
            >

                <el-form-item label="Account :" prop="username" style="text-align: center">
                    <el-input v-model="Data.submitForm.username" />
                </el-form-item>
                <el-form-item label="Password :" prop="password" style="text-align: center">
                    <el-input v-model="Data.submitForm.password" type="password"/>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm(ruleFormRef)"
                        >Submit</el-button
                    >
                <!-- <el-button @click="resetForm(ruleFormRef)">Reset</el-button> -->
                </el-form-item>
                <div class="signup">
                    <p class="desc">
                        Do not have an account?
                        <router-link to="/sign-up"> SignUp</router-link>
                    </p>
                </div>
        </el-form>
    </div>
</template>

<script lang="ts" setup>
import { ref, reactive, getCurrentInstance, watch } from 'vue'
import { ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router"
import { useStore } from "vuex"
import axios from 'axios';

const API = (getCurrentInstance() as any).proxy.api
const router = useRouter()

const store = useStore()

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input the password'))
  } else {
    if (ruleForm.checkPass !== '') {
      if (!ruleFormRef.value) return
      ruleFormRef.value.validateField('checkPass', () => null)
    }
    callback()
  }
}

const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input the password again'))
  } else if (value !== ruleForm.password) {
    callback(new Error("Two inputs don't match!"))
  } else {
    callback()
  }
}

const ruleForm = reactive({
    username: '',
    password: '',
    checkPass: '',
})

const ruleFormRef = ref('')

let Data = reactive({
    submitForm: reactive({
            username: '',
            password: '',
    })
})

const submit = async () =>{
                // axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem("token")
                await API.login.addData(Data.submitForm).then((res)=>{
                    console.log(res)
                        const token = res.data.auth_token
                        store.commit("setToken", token)
                        // axios.defaults.headers.common["Authorization"] = "Token " + token
                        localStorage.setItem("token", token)
                        ElMessage({
                            message:"Add successfully!",
                            type:'success'
                        })            
                })
                .catch(error => {
                            if (error.response) {
                                    console.log(error)
                                    ElMessage({
                                                message: error.response.data,
                                                type:'error'
                                            })
                                }else if (error.message){
                                    console.log('Something went wrong. Please try again!')
                                }
                        })

                await API.account.getData().then(res =>{
                        store.commit('setUser', {'id': res.data.id, 'username':res.data.username})
                        localStorage.setItem('username', res.data.username)
                        localStorage.setItem('userid', res.data.id)
                        console.log(localStorage)
                        router.push("/home")
                })
                .catch(error => {
                    console.log(error)
            })
}
const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate((valid, fields) => {
        if (valid) {
                    submit()
        } else {
            console.log('error submit!', fields)
        }   
    })
}
</script>

<style scoped>
:deep(.el-form-item__label){
    color: #00ff00;
}
.el-input{
    --el-input-bg-color:black;
    --el-input-focus-border-color:#00ff00;
    --el-input-focus-border:#00ff00;
}
:deep(.el-input__inner){
    color: #00ff00
}
.el-button--primary{
    --el-button-hover-bg-color:#00ff00;
    --el-button-hover-text-color:black;
    --el-button-bg-color:black;
    --el-button-text-color:#00ff00;
    --el-button-border-color:white
}
.el-button{
    --el-button-bg-color:black;
    --el-button-text-color:#00ff00;
    --el-button-hover-bg-color:#00ff00;
    --el-button-hover-text-color:black;
}
.card{
    text-align:center
}
.card{
    display: flex;
    flex-direction: column;
    /* align-items: center; */
}
.desc{
    color:#00ff00;
    margin-left: 110px
}
</style>