<template>
  <div>
    <div class="container" style="text-align: left;">
      <div class="row">
        <Section :name="'Todo'" :status="'TODO'" :data='todos' :onDrop="onDrop" :dragstart="startDrag"/>
        <Section :name="'Doing'" :status="'DOING'" :data='doing' :onDrop="onDrop" :dragstart="startDrag" />
        <Section :name="'Done'" :status="'DONE'" :data='done' :onDrop="onDrop" :dragstart="startDrag" /> 

      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Todo, StatusEnum } from "../model"
import Card from "./Card.vue"
import Section from "./Section.vue"

export default {
  name: 'Board',
  props: {
    data: Array,
    updateStatus: Function
  },
  components: {
    Section
  },
  data() {
    return {
      todos: [],
      doing: [],
      done: [],
    }
  },
  created() {
    this.separateTodos()
  },
  watch: {
    data: function(o, n) {
      this.separateTodos()
    }
  },
  methods: {
    startDrag: (evt, todo) => {
      evt.dataTransfer.dropEffect = 'move'
      evt.dataTransfer.effectAllowed = 'move'
      evt.dataTransfer.setData('todoId', todo.id)
    },
    onDrop (evt, status) {
      const todoId = evt.dataTransfer.getData('todoId')
      const todo = this.data.find(todo => todo.id == todoId)
      todo.status = status
      this.updateStatus(todoId, status)
      this.separateTodos()
    },
    separateTodos() {
      this.todos = this.data.filter(todo => todo.status === StatusEnum.TODO)
      this.doing = this.data.filter(todo => todo.status === StatusEnum.DOING)
      this.done = this.data.filter(todo => todo.status === StatusEnum.DONE)
    }
  }
}
</script>
