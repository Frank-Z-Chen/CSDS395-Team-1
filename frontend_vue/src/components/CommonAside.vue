<template>
   <el-menu 
   default-active="1-4-1" 
   class="el-menu-vertical-demo" 
   unique-open=true 
   background-color="#545c64" 
   text-color="white" 
   active-text-color="#ffd04b" 
   :collapse="isCollapse">
    <h3>Wiki</h3>
    <el-menu-item @click="clickMenu(item)" v-for="item in allChoice" :index="item.path" :key="item.path">
      <i :class="'el-icon-' + item.icon"></i>
      <span slot="title">{{item.label}}</span>
    </el-menu-item>
  </el-menu>
      
</template>

<style lang="less" scope>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
    }
    .el-menu {
      height: 100vh;
      border: none;
      h3 {
        color: #fff;
        text-align: center;
        line-height: 48px;
      }
    }
</style>

<script>
  export default {
    data() {
      return {
        isCollapse: false,
        menu: [
          {
            path: '/',
            name: 'home',
            label: 'Introduction',
            icon: 'document',
            url: 'intro/intro'
          },
          {
            path: '/char',
            name: 'char',
            label: 'Characters',
            icon: 's-custom',
            url: 'char/char'
          },
          {
            path: '/item',
            name: 'item',
            label: 'Items',
            icon: 'menu',
            url: 'items/items'
          },
          {
            path: '/mons',
            name: 'mons',
            label: 'Monsters',
            icon: 'close',
            url: 'mons/mons'
          },
          {
            path: '/weap',
            name: 'weap',
            label: 'Weapons',
            icon: 's-flag',
            url: 'weap/weap'
          },
          {
            path: '/more',
            name: 'more',
            label: 'More',
            icon: 'more',
            url: 'more/more'
          },
          {
            path: '/edit',
            name: 'edit',
            label: 'Page Edit',
            icon: 'document-add',
            url: 'edit/edit'
          }
        ]
      };
    },
    methods: {
      clickMenu(item){
        this.$router.push({
          name: item.name
        })
      }
    },
    computed: {
      allChoice() {
        return this.menu
      }
    }
  }
</script>