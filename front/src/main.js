import { createApp } from 'vue'
import App from './App.vue'
import vueKanban from 'vue-kanban'
import 'vue-kanban/src/assets/kanban.css'

createApp(App).use(vueKanban).mount('#app')
