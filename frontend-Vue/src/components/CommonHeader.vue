<template>
    <header>
        <div class="l-content">
            <h3 style="color:#fff">Banner of the Maid</h3>
        </div>
        <div class="r-content">
            <el-dropdown trigger="click" size="mini">
                <span>
                    <img class="user" :src="userImg">
                </span>
                <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>User Center</el-dropdown-item>
                <el-dropdown-item>Log out</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </header>
</template>

<script>
    export default{
        name: 'CommonHeader',
        data() {
            return{
                userImg: require('../assets/image/logo.png')
            }
        }
    }
</script>

<style lang="less" scoped>
    header {
        display: flex;
        height: 100%;
        justify-content: space-between;
        align-items: center;
    }
    .l-content{
        display: flex;
        align-items: center;
        font-style: italic;
    }
    .r-content {
        display: flex;
        align-items: center;
        .user {
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }
    }
</style>
