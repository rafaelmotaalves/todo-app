<template>
    <div class="modal fade" id="createTodoModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
        <div class="modal-header"> 
            Create todo
        </div>
        <div class="modal-body">
            <div class="input-group mb-3">
                <input v-model="title" type="text" class="form-control" placeholder="Title" aria-label="title" aria-describedby="basic-addon1">
            </div>
            <div class="input-group mb-3">
                <textarea v-model="description" placeholder="Description" class="form-control" aria-label="Description"></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button v-on:click="submit()" type="button" class="btn btn-primary">Save changes</button>
        </div>
        </div>
    </div>
    </div>
</template>

<script lang="ts">
export default {
    name: "CreateTodoModal",
    props: {
        visible: Boolean,
        onSave: Function
    },
    data() {
        return {
            title: "",
            description: ""
        }
    },
    methods: {
        submit() {
            this.onSave(this.title, this.description)
            $("#createTodoModal").modal("toggle")
        }
    }
}
</script>
