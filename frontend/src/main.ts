import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from '../router'
import * as Icons from "@element-plus/icons-vue"
import store from '../store'
import api from '../api'

const app = createApp(App)
for (const [key, component] of Object.entries(Icons)){
    app.component(key, component)
}
app.use(router).use(store).use(ElementPlus).mount('#app')
app.config.globalProperties.api = api
// iterate all icons and import to component tag
// Object.keys(Icons).forEach((key) => {
//     app.component(key, Icons[key as keyof typeof Icons])
// })