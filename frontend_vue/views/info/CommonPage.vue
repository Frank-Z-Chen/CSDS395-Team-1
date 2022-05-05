<template>
    <div>
        {{ content }}
    </div>
</template>

<script>
import information from "../mons/index.vue"
    export default{
        name: 'item',
        data(){
            return {
                content: null
            }
        },
        mounted(){
            this.content = information.information
        }
    }
</script>
