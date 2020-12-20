<template>
  <div>
    <button type="button" class="btn btn-success" data-toggle="modal" data-target="#createTodoModal">
      Create todo
    </button>
    <div class="container" style="text-align: left;">
      <div class="row">
        <Section :name="'Todo'" :status="'TODO'" :data='todos' :onDrop="onDrop" :dragstart="startDrag"/>
        <Section :name="'Doing'" :status="'DOING'" :data='doing' :onDrop="onDrop" :dragstart="startDrag" />
        <Section :name="'Done'" :status="'DONE'" :data='done' :onDrop="onDrop" :dragstart="startDrag" /> 
      </div>
    </div>
    <CreateTodoModal :onSave="createTodo"/>
  </div>
</template>

<script lang="ts">
import { Todo, StatusEnum } from "../model"
import Card from "./Card.vue"
import Section from "./Section.vue"
import CreateTodoModal from "./CreateTodoModal.vue"
import * as api from "../api"

export default {
  name: 'Board',
  props: {},
  components: {
    Section,
    CreateTodoModal
  },
  data() {
    return {
      data: [],
      todos: [],
      doing: [],
      done: [],
    }
  },
  created() {
    this.fetchData()
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
    },
    fetchData() {
      api.getAllTodos()
        .then(data => {
          this.data = data;
        })
        .catch(console.log)
    },
    updateStatus(todoId: number, status: StatusEnum) {
      api.updateStatus(todoId, status);
    },
    createTodo(title: string, description: string) {
      api.createTodo(title, description)
        .then(this.fetchData)
    }
  }
}
</script>
