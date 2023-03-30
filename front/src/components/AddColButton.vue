<template>
    <div>
        <button @click="showForm = true">Add Column</button>
        <div v-if="showForm">
            <form>
                <!-- Form fields for creating a new column -->
                <label for="title">Column Title</label>
                <input  v-model="newTitle" type="text" name="title" id="title">
                <button @click="createCol">Envoyer</button>
            </form>
            <button @click="showForm = false">Close</button>
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
        }

    }

 }
</script>