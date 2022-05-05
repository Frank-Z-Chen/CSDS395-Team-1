<template>
    <header>
        <div class="l-content">
            <h3 style="color:#fff">Banner of the Maid</h3>
        </div>
        <div class="r-content">
            <el-dropdown trigger="click" size="mini" @command="handle">
                <span>
                    <img class="user" :src="userImg">
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="usercenter">User Center</el-dropdown-item>
                    <el-dropdown-item command="login">Log out</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </header>
</template>

<script>
    export default {
        name: 'CommonHeader',
        data() {
            return{
                userImg: require('../assets/image/logo.png'),
                titleImg: require('../assets/image/title.png')
            };
        },
        methods: {
            handle(command) {
                this.$router.push(command)
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
    h3 {
        font-family: 'Times New Roman', Times, serif;
    }
    .l-content{
        display: flex;
        align-items: center;
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
