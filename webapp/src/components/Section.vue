<template>
    <div class="col-sm">
        {{ name }}
        <div @drop="onDrop($event, status)" @dragover.prevent @dragenter.prevent class="drop-zone">
            <Card draggable="true" @dragstart="dragstart($event, todo)" :key="todo.id" v-for="todo in data" :data="todo" class="drag-el" />
        </div>
    </div>
</template>

<style scoped>
  .drop-zone {
    background-color: #eee;
    margin-bottom: 10px;
    padding: 10px;
    height: 80vh;
  }

  .drag-el {
    background-color: #fff;
    margin-bottom: 10px;
    padding: 5px;
  }
  
</style>

<script lang='ts'>
import { StatusEnum } from '../model'
import Card from './Card.vue'

export default {
    name: "Section",
    props: {
        status: StatusEnum,
        name: String,
        data: Array,
        dragstart: Function,
        onDrop: Function
    },
    components: {
        Card
    }    
}
</script>