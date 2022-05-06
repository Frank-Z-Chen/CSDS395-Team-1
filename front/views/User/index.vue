<template>
    <div class="manage">
        <el-dialog
            :title="operateType === 'add' ? 'Add new user' : 'Update user'"
            :visible.sync="isShow">
            <common-form
                :formLabel="operateFormLabel"
                :form="operateForm"
                :inline="true"
                ref = "form">
            </common-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="isShow = false">Cancel</el-button>
                <el-button type="primary" @click="confirm">Confirm</el-button>
            </div>
        </el-dialog>
        <div class="manage-header">
            <el-button type="primary" @click="addUser">+ add</el-button>
            <common-form
                :formLabel="formLabel"
                :form="searchForm"
                :inline="true"
                ref = "form">
                <el-button type="primary" @click="getList">Search</el-button>
            </common-form>
        </div>
    </div>
</template>

<script>
import CommonForm from '../../src/components/CommonForm.vue'
    export default {
        name: 'User',
        components: {
            CommonForm
        },
        data(){
            return {
                operateType: 'add',
                isShow: false,
                operateFormLabel: [
                    {
                        model: 'name',
                        label: 'Name',
                        type: 'input'
                    },
                    {
                        model: 'date',
                        label: 'Date',
                        type: 'date'
                    }
                ],
                operateForm: {
                    name: '',
                    date: ''
                },
                formLabel:[
                    {
                        model: "keyword",
                        label: '',
                        type: 'input'
                    }
                ],
                searchForm:{
                    keyword: ''
                }
            }
        },
        methods: {
            confirm(){
                if (this.operateType === 'edit'){
                    this.$http.post('/user/edit', this.operateForm).then(res => {
                        this.isShow = false
                    })
                }
                else {
                    this.$http.post('/user/add', this.operateForm).then(res => {
                        this.isShow = false
                    })
                }
            },
            addUser(){
                this.isShow = true
                this.operateType = 'add'
                this.operateForm = {
                    name: '',
                    date: ''
                }
            },
            getList(){

            }
        }
    }
</script>

<style lang="less" scoped>
.manage-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

</style>