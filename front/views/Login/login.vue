<template>
    <el-form
        :model="form"
        status-icon
        :rules="rules"
        ref="form"
        label-width="100px"
        class="login-container"
    >
        <h3 class="login_title">
            Login
        </h3>
        <el-form-item
            label = "User"
            label-width = "80px"
            prop = "username"
            class="username"
        >
            <el-input
                type="input"
                v-model="form.username"
                auto-complete="off"
                placeholder="Please enter the user name">
            </el-input>
        </el-form-item>

        <el-form-item
            label = "Password"
            label-width = "80px"
            prop = "password"
        >
            <el-input
                type="password"
                v-model="form.password"
                auto-complete="off"
                placeholder="Please enter the password">
            </el-input>
        </el-form-item>
        <el-form-item class="login_submit">
            <el-button type="primary" @click="login">
                Login
            </el-button>
        </el-form-item>
    </el-form>
</template>

<script>
const baseUrl = 'http://localhost:8000'
import axios from "axios"
import { Notification } from 'element-ui';

    export default{
        name: 'login',
        data(){
            return {
                form: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        {required: true, message: "Please enter the user name", trigger: "blur"},
                        {
                            min:3,
                            message: "User name cannot be less than 3 digits",
                            trigger: "blur"
                        }
                    ],
                    password: [
                        {required: true, message: "Please enter the password", trigger: "blur"}
                    ]
                }
            }
        },
        methods: {
            login() {
                const path = baseUrl + '/api/login/'
                const data = {
                    email: this.form.username,
                    password: this.form.password
                }
                axios.post(path, data).then(() => {
                    this.$router.push({name: 'home'})
                }).catch(e => {
                    Notification.error(e.response.data.detail)
                })
            }
        }
    }
</script>

<style lang="less" scoped>
    .login-container {
        border-radius: 15px;
        background-clip: padding-box;
        margin: 180px auto;
        width: 350px;
        padding: 35px 35px 15px 35px;
        background-color: #fff;
        border: 1px solid #000000;
        box-shadow: 0 0 25px #9a9a9b;
    }

    .login_title {
        margin: 0px auto 40px auto;
        text-align: center;
        color: #505458;   
    }

    .login_submit {
        margin: 10px 100px 0px auto;
        text-align: center;
    }
</style>