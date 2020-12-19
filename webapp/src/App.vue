<template>
  <Board
    :data="data"
    :updateStatus="updateStatus"
    />
</template>

<script lang="ts">
import Board from './components/Board.vue'
import { StatusEnum, Todo } from './model'
import * as api from "./api"

export default {
  name: 'App',
  components: {
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
    }
  }
}
</script>
