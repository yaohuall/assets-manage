import axios from "axios"

const request = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    timeout: 10000,
})

// === 请求拦截器（request）======
request.interceptors.request.use(
    (config: any) => {
        // 获取本地loalstorage中的token 
        let token = localStorage.getItem('token')
        // 判断是否有token
        if (token) {
            config.headers.common['Authorization'] = 'Token ' + token;
        }
        else{console.log('no token!')}
        // 返回return 
        return config
    },
    (error: any) => {
        Promise.reject(error);
    }
)

export default request