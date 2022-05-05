<template>
    <div class="main">
        <el-carousel :interval="4000" type="card">
            <el-carousel-item v-for="item in images" :key="item">
                <!-- <h3 class="medium">{{ item }}</h3> -->
                <!-- <img :src = "userImg" width="100%"> -->
                <img :src="item.url" width="100%">
            </el-carousel-item> 
        </el-carousel>
        <div class="intro">
            <div class ="title">Introduction</div><br/><br/>
            Banner of the Maid is a mix of turn-based strategy and JRPG. Set in an alternate French Revolution with fantasy elements, as the young officer Pauline Bonaparte you will have to lead your troops to battle and play a role in the political vortex of Paris.
        </div>
    </div>
    
</template>

<style scoped>
    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }
    
    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }
    
    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
    .main {
        margin: 75px;
    }
    .intro{
        display: flex;
        align-items: left;/* 
        font-style: italic; */
        font-family: 'Times New Roman', Times, serif;
        font-size: 25px;
        margin-right: 50px;
    }
    .title{
        font-size: 50px;
    }
</style>

<script>
    export default{
        name: 'home',
        data(){
            return {
                userImg: require('../../src/assets/image/1.png'),
                images:[
                    {url: require('../../src/assets/image/1.png')},
                    {url: require('../../src/assets/image/2.jpg')},
                    {url: require('../../src/assets/image/3.png')}
                ]
            }
        }
    }
</script>
