<template>
    <label for="col-modal" class="btn h-auto w-20 my-2 mx-2">
        <span class="text-2xl font-bold text-white">+</span> 
        Ajouter une Colonne
    </label>
    <input type="checkbox" id="col-modal" class="modal-toggle"/>

    <div class="modal">
        <div class="modal-box">

            <label for="col-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
            <h2 class="mb-4">Ajouter une colonne</h2>

            <!-- Form fields for creating a new column -->
            <form class="grid grid-flow-row ">
                
                <label for="title" class="mb-2 ">Column Title</label>
                <input  v-model="newTitle" type="text" name="title" id="title">
                <div class="modal-action">
                    <button class="btn" @click="createCol">Envoyer</button>
                </div>
            </form>
            
        </div>
    </div>
</template>

<script>
 export default {
    name : 'AddColButton',
    props: {
        stages: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            newTitle:'',
            position:0,
            showForm: false
        }
    },
    methods:{
        async createCol(){
            this.position = this.stages.length
            var item = {
                title: this.newTitle,
                pos:this.position
            }

            await fetch('http://localhost:8000/api/col/',{
                method:'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(item)   
            });

            this.$emit('col-created');
        }

    }

 }
</script>