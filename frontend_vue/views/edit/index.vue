<template>
  <body>
    <el-upload
    class="upload-demo"
    drag
    action="http://127.0.0.1:8000/wiki/ocr/type1/page-1/"
    multiple = "false">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">Please drag the file, or <em>click here</em> to choose a file</div>
      <div class="el-upload__tip" slot="tip">Only support jpg/png file</div>
    </el-upload>
    <el-button @click="getPic()">
      Get
    </el-button>
   </body>
   
</template>

<style scoped>
  body {
    display: flex;
    height: 100%;
    justify-content: space-between;
    margin: 50px;
  }
</style>

<script>
import axios from 'axios';
    export default{
        name: 'edit',
        data(){
            return {
              information:null
            }
        },
        methods: {
          getPic(){
            axios
            .post("http://127.0.0.1:8000/wiki/ocr/type1/page-1/")
            .then(response => {
              this.information = JSON.stringify(response)
            })
            {{ information }}
            console.log("1")
          }
        }
    }
</script>
