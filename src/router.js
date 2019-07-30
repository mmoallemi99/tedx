import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Team from './views/Team.vue'
import Sponsors from './views/Sponsors.vue'
import Nominate from './views/Nominate.vue'

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/', component: Home, name: 'home', },
    { path: '/team', component: Team, name: 'team', },
    { path: '/sponsors', component: Sponsors, name: 'sponsors', },
    { path: '/nominate', component: Nominate, name: 'nominate', },
    { path: '*', redirect: '/' },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})
