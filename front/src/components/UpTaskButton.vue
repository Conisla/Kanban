<template>
    
    <label for="up-task-modal" class="w-8 mb-2">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABwElEQVR4nO2ZPUvEMByH/zo4uLu7iahfQE4EQXBw9OUE/QZ+AME73TydXHwDPceb1cFB8AsIDn4CB+/cRUHEl0dypBJqy3ln00sgz9Q2bZqnvySkrYgjAFPADfAFPAGXwIj4BFAEPviNEhoWHwDmgHfSORPXAeYNiV3gPkHkWTyS2NTHBhNk3BUBFgyJjVjZYEzmQnyTUAC9QE2XvwCj4hrAoiFRTpGo6vJXYFocHxNJSfQAh7r8DZht9wZ9wA7wSPZU9VM2kygltEGdc2IkMQP0A9ct6m8A28pB9AYWJYqWJEwqoq0U4+13mJZpmxLrKRLHpoS0V39BX9tQO00sz07llDFx0PGY0Py034bIHyX2/ythVSQmUbIpYU0kbwkrIt2QyFwEmDTeJ9ZSJI46nZ3yFImm0FqeEjZEotWqSmU5JrGXdXeyIgIMRXUYMit5SGQtshoTiWSubHUnWyLnpGMtiUxF9FpJfekw+QRu1UIOGOuk3m6J3AEPwCmwBAxIjpBV1+o2BBHHICTiGIREHIOQiGMQEnEMQiIOJ9LQ2wXxDGBCt70u+r3Bd7ai3woVIxmfqCuJ5m+FQCAQCAQCIt849qNkWXTyNAAAAABJRU5ErkJggg==">
    </label>
    <input type="checkbox" id="up-task-modal" class="modal-toggle"/>
    
    <div v-if="block" class="modal">
        <div class="modal-box">
            
            <label for="up-task-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
            <h2 class="mb-4">Modifier la tache {{ task.title }}</h2>

            <form class="grid grid-flow-row ">
                
                <label for="title">Task Title</label>
                <input  v-model="task.title" type="text" name="title" id="title">
                
                <label for="descr">Task Description</label>
                <input  v-model="task.descr" type="text" name="descr" id="descr">
                
                <div class="modal-action">
                    
                    <button class="btn" @click="UpdateTaskInfo(this.task)">Envoyer</button>
                </div>
            </form>
            
        </div>
    </div>
</template>     

<script>
export default {
    name: 'UpTaskButton',
    props:{
        block: {
            type: Object,
            required: true,
        },
    },
    data(){
        return{
            task: this.block,
        }
    },
    methods:{
        async UpdateTaskInfo(){
            var task = {
                title:this.task.title,
                descr:this.task.descr
            }
            
            await fetch('http://localhost:8000/api/task/'+this.task.id+'/',{
                method:'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(task)
                
            });
            this.getBoard()
        },
    }
    
}
</script>
