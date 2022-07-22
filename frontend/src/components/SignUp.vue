<template>
    <div class="card">
        <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                label-width="200px"
                class="demo-ruleForm"
                status-icon
                :rules="Data.rules"
                style="width: 25%"
            >

                <el-form-item label="Account :" prop="username" style="text-align: center">
                    <el-input v-model="ruleForm.username" />
                </el-form-item>
                <el-form-item label="Password :" prop="password" style="text-align: center">
                    <el-input v-model="ruleForm.password" type="password"/>
                </el-form-item>
                <el-form-item label="Confirm password :" prop="checkPass" style="text-align: center">
                    <el-input v-model="ruleForm.checkPass" type="password" />
                </el-form-item>
                <el-form-item>
                <el-button type="primary" @click="submitForm(ruleFormRef)"
                    >Submit</el-button
                >
                <!-- <el-button @click="resetForm(ruleFormRef)">Reset</el-button> -->
                </el-form-item>
        </el-form>
    </div>
</template>

<script lang="ts" setup>
import { ref, reactive, getCurrentInstance, watch } from 'vue'
import { ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router"

const API = (getCurrentInstance() as any).proxy.api
const router = useRouter()

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
        rules: reactive({
            username: [
                        { required: true, message: 'Please input user account', trigger: 'blur' },
                        { min: 6, message: 'Length should be at least 6', trigger: 'blur' },
                ],
            password: [
                    { required: true, message: 'Please input password', trigger: 'blur' },
                    { validator: validatePass, trigger: 'blur' }
                ],
            checkPass: [
                    { required: true, message: 'Please confirm password', trigger: 'blur' },
                    { validator: validatePass2, trigger: 'blur' }
                ],
    }),
})

const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return
    await formEl.validate((valid, fields) => {
        if (valid) {
                API.sign.addData(ruleForm).then((res)=>{
                    ElMessage({
                        message:"Add successfully!",
                        type:'success'
                    })
                    router.push("/log-in")
            })
            .catch(error => {
                        if (error.response) {
                                // console.log(`${property}: ${error.response.data[property]}`)
                                ElMessage({
                                            message: error.response.data,
                                            type:'success'
                                        })
                            }else if (error.message){
                                console.log('Something went wrong. Please try again!')
                            }
                    })
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
</style>