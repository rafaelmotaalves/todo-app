<template>
  <div>
    <button type="button" class="btn btn-success" data-toggle="modal" data-target="#createTodoModal">
      Create todo
    </button>
      <Board
    :data="data"
    :updateStatus="updateStatus"
    />

    <CreateTodoModal :onSave="createTodo"/>
  </div>
</template>

<script lang="ts">
import CreateTodoModal from './components/CreateTodoModal.vue'
import Board from './components/Board.vue'
import { StatusEnum, Todo } from './model'
import * as api from "./api"

export default {
  name: 'App',
  components: {
    CreateTodoModal,
    Board
  },
  data: () => ({
    data: [],
    todos: [],
    doing: [],
    done: []
  }),
  created () {
    this.fetchData()
  },
  methods: {
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
