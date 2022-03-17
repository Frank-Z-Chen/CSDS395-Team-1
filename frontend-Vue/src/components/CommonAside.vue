<template>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" unique-open=true @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <el-menu-item index="1">
            <template slot="title">
                <i class="el-icon-document"></i>
                <span slot="title">Introduction</span>
            </template>
            <!-- <el-menu-item-group>
                <span slot="title">Group1</span>
                <el-menu-item index="1-1">选项1</el-menu-item>
                <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group2">
                <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
                <span slot="title">选项4</span>
                <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu> -->
        </el-menu-item>
        <el-menu-item index="2">
            <i class="el-icon-s-custom"></i>
            <span slot="title">Characters</span>
        </el-menu-item>
        <el-menu-item index="3">
            <i class="el-icon-menu"></i>
            <span slot="title">Items</span>
        </el-menu-item>
        <el-menu-item index="4">
            <i class="el-icon-close"></i>
            <span slot="title">Monsters</span>
        </el-menu-item>
        <el-menu-item index="5">
            <i class="el-icon-s-flag"></i>
            <span slot="title">Weapons</span>
        </el-menu-item>
        <el-menu-item>
          <i class="el-icon-more"></i>
          <span slot="title">More</span>
        </el-menu-item>
    </el-menu>
</template>

<style>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
    }
</style>

<script>
  export default {
    data() {
      return {
        isCollapse: false
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>