<template>
  <div class="card" style="text-align: left; ">
    <div class="card-body">
      <h5 class="card-title">{{ data.title }}</h5>
      <p class="card-text">{{ data.description }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { Todo } from "../model"

export default {
    name: "Card",
    props: {
      data: Todo
    }
}
</script>