import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from '../router'
import axios from 'axios';

Vue.use(ElementUI);
Vue.config.productionTip = false
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://127.0.0.1:8000'

// router.beforeEach((to, from, next) => {
//   store.commit('getToken')
//   const token = store.state.user.token
//   if (!token && to.name !== 'login'){
//     next({name: 'login'})
//   }
//   else{
//     next()
//   }
// })


new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
