<template>
    <div class="container list-group" style="text-align: left;">
        <h1>Boards</h1>
        <router-link :to="{ name: 'board', params: { id: board.id }}" v-for="board in boards" :key="board.id" >
            <div class="list-group-item list-group-item-action" >{{ board.title }}</div>
        </router-link>
    </div>
</template>

<script lang="ts">
import * as api from "../api"

export default {
    name: 'Home',
    data() {
        return {
            boards: []
        }
    },
    created() {
        this.fetchData()
    },
    methods: {
        fetchData() {
            api.getBoards()
                .then(data => {
                    this.boards = data
                }).catch(console.log)
        }
    }
}
</script>