<template>
    <div>
        <button @click="showForm = true">Add Task</button>
        <div v-if="showForm">
            <form>
                <label for="title">Task Title</label>
                <input  v-model="newTitle" type="text" name="title" id="title">
                <label for="descr">Task Description</label>
                <input  v-model="newDescr" type="text" name="descr" id="descr">
                <button type="submit" @click="createTask">Envoyer</button>
            </form>
            <button @click="showForm = false">Close</button>
        </div>
    </div>
</template>

<script>
 export default {
    name : 'AddTaskButton',
    props:{
        blocks: {
            type: Array,
            required: true,
        },
        board: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            newTitle:'',
            newDescr:'',
            position:0,
            idCol:0,
            showForm: false,
        }
    },
    methods:{
        async createTask(){

            this.position = this.board[0].taches.length
            this.idCol = this.board[0].id_col

            var item = {
                title: this.newTitle,
                descr: this.newDescr,
                pos:this.position,
                id_col:this.idCol
            }

            await fetch('http://localhost:8000/api/task/',{
                method:'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(item)   
            });
        }
    }
 }
</script>