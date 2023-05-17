import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.directive('myfocus', {
    mounted: (el, binding) => {
        if (binding.value == true || binding.value == undefined) {
            el.focus()
        }
    }
})

app.use(router)

app.use(ElementPlus)

app.mount('#app')
