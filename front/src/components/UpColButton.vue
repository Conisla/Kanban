<template>
    <label for="up-col-modal" class="w-8 mb-2">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABwElEQVR4nO2ZPUvEMByH/zo4uLu7iahfQE4EQXBw9OUE/QZ+AME73TydXHwDPceb1cFB8AsIDn4CB+/cRUHEl0dypBJqy3ln00sgz9Q2bZqnvySkrYgjAFPADfAFPAGXwIj4BFAEPviNEhoWHwDmgHfSORPXAeYNiV3gPkHkWTyS2NTHBhNk3BUBFgyJjVjZYEzmQnyTUAC9QE2XvwCj4hrAoiFRTpGo6vJXYFocHxNJSfQAh7r8DZht9wZ9wA7wSPZU9VM2kygltEGdc2IkMQP0A9ct6m8A28pB9AYWJYqWJEwqoq0U4+13mJZpmxLrKRLHpoS0V39BX9tQO00sz07llDFx0PGY0Py034bIHyX2/ythVSQmUbIpYU0kbwkrIt2QyFwEmDTeJ9ZSJI46nZ3yFImm0FqeEjZEotWqSmU5JrGXdXeyIgIMRXUYMit5SGQtshoTiWSubHUnWyLnpGMtiUxF9FpJfekw+QRu1UIOGOuk3m6J3AEPwCmwBAxIjpBV1+o2BBHHICTiGIREHIOQiGMQEnEMQiIOJ9LQ2wXxDGBCt70u+r3Bd7ai3woVIxmfqCuJ5m+FQCAQCAQCIt849qNkWXTyNAAAAABJRU5ErkJggg==">
    </label>
    <input type="checkbox" id="up-col-modal" class="modal-toggle"/>
    
    <div v-if="stage.length>1" class="modal">
        <div class="modal-box">
            
            <label for="up-col-modal" class="btn btn-sm btn-circle absolute right-2 top-2">✕</label>
            <h2 class="mb-4">Modifier la colonne</h2>

            <form class="grid grid-flow-row ">
                
                <label for="title">Column Title</label>
                <input  v-model="col.title" type="text" name="title" id="title">

                <div class="modal-action">
                    
                    <button class="btn" @click="UpdateColInfo()">Envoyer</button>
                </div>
            </form>
            
        </div>
    </div>
</template>     

<script>

export default {
    name: 'UpColButton',
    props:{
        stage: {
            type: String,
            required: true,
        },
        board: {
            type: Array,
            required: true,
        },
    },
    methods:{
        async UpdateColInfo(){
        var col= {
                title: this.stage,
                pos: this.board.find(c => c.title == this.stage).pos,
            }
        let idCol = this.board.find(c => c.title == this.stage).id_col

        console.log(col);
        console.log(idCol);

        await fetch('http://localhost:8000/api/col/'+idCol+'/',{
            method:'put',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(col)
        });
        this.getBoard()
        },
        }
    
}
</script>
