<template>
  <body>
    <div>{{ info }}</div>
    <div>{{ printlist }}</div>
    <el-link @click="ask(item)" v-for="item in printlist" :index="item" :key = "item">
      {{ item }}
    </el-link>
    <div><br/>
      <el-upload
        class="upload-demo"
        drag
        action="http://127.0.0.1:8000/wiki/ocr/type1/page-1/"
        multiple = "false">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">Please drag the file, or <em>click here</em> to choose a file</div>
        <div class="el-upload__tip" slot="tip">Only support jpg/png file</div>
      </el-upload>
    </div>
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
        name: 'item',
        data(){
            return {
                info: null,
                printlist:[],
                indexlist:[],
                information:null
            }
        },
        mounted (){
            axios
            .get('../wiki/page/type1/')
            .then(response => {
              this.info = Object.values(response)[0].length
              for (let i=0; i < Object.values(response)[0].length; i++){
                this.printlist[i] = Object.values(Object.values(Object.values(response)[0])[i])[1]
              }
            })
        },
        methods: {
          ask(item){
            axios
            .get("../wiki/page/type1/" + item + "/")
            .then(response => {
              information = JSON.stringify(response)
            })
          }

          /* getData(){
            alert('111')
            this.$axios
            .get('../wiki/page/type1/name1/')
            .then(successResponse => {
              if (successResponse.data.code === 200) {
                var jsonObj = JSON.parse(JSON.stringify(successResponse.data.data));
                var newArray= new Array()
                for (var i = 0; i < jsonObj.length; i++){
                  jsonObj[i].index='table'
                }
                this.item[1].subs=jsonObj;
                console.log(this.item[1].subs);
              }
            })
          } */
        },
        computed:{
          allChoice(){
            return this.printlist
          }
        }
    }
</script>
