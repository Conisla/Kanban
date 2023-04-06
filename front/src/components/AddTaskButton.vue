<template>

    <label for="task-modal" class="btn flex w-64 space-x-8 mb-2 mx-2">
        <span class="text-2xl font-bold text-white">+</span> 
       <p> Ajouter une tache</p>
    </label>
    <input type="checkbox" id="task-modal" class="modal-toggle"/>

    <div class="modal">
        <div class="modal-box">

            <label for="task-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
            <h2 class="mb-4">Ajouter une tache</h2>

            <!-- Form fields for creating a new column -->
            <form class="grid grid-flow-row ">
                <label for="title">Task Title</label>
                <input  v-model="newTitle" type="text" name="title" id="title">
                <label for="descr">Task Description</label>
                <input  v-model="newDescr" type="text" name="descr" id="descr">
                <div class="modal-action">
                    <button class="btn" @click="createTask">Envoyer</button>
                </div>
            </form>
            
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
            idCol:-1,
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