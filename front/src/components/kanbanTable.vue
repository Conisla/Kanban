<!-- Tableau Kanban de vue-kanban personaliser avec v-slot -->

<template>
  <AddTaskButton :blocks="blocks" :board="board"/>
  
  <div id="board-container" class="flex overflow-x-auto flex-shrink-0">
    <div v-if="board.length>0" class="">
      <kanban-board :stages="stages" :blocks="blocks" :board="board" @update-block="updateBlock" @drop="Droped">
        
        <!-- template pour une colonne -->
        <template v-for="stage in board" :key=stage v-slot:[stage.title]>
          <h3>{{ stage.title }}</h3>
          <div class="flex flex-col">
            <!-- <UpColButton :stage="stage" :board="board"/> -->
            <button class="m-auto w-8 mb-2" @click="ShowUpdateCol(stage)">
              <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABwElEQVR4nO2ZPUvEMByH/zo4uLu7iahfQE4EQXBw9OUE/QZ+AME73TydXHwDPceb1cFB8AsIDn4CB+/cRUHEl0dypBJqy3ln00sgz9Q2bZqnvySkrYgjAFPADfAFPAGXwIj4BFAEPviNEhoWHwDmgHfSORPXAeYNiV3gPkHkWTyS2NTHBhNk3BUBFgyJjVjZYEzmQnyTUAC9QE2XvwCj4hrAoiFRTpGo6vJXYFocHxNJSfQAh7r8DZht9wZ9wA7wSPZU9VM2kygltEGdc2IkMQP0A9ct6m8A28pB9AYWJYqWJEwqoq0U4+13mJZpmxLrKRLHpoS0V39BX9tQO00sz07llDFx0PGY0Py034bIHyX2/ythVSQmUbIpYU0kbwkrIt2QyFwEmDTeJ9ZSJI46nZ3yFImm0FqeEjZEotWqSmU5JrGXdXeyIgIMRXUYMit5SGQtshoTiWSubHUnWyLnpGMtiUxF9FpJfekw+QRu1UIOGOuk3m6J3AEPwCmwBAxIjpBV1+o2BBHHICTiGIREHIOQiGMQEnEMQiIOJ9LQ2wXxDGBCt70u+r3Bd7ai3woVIxmfqCuJ5m+FQCAQCAQCIt849qNkWXTyNAAAAABJRU5ErkJggg==">
            </button>
            <button class="m-auto" @click="deleteCol(stage.id_col)">
              <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
              width="24" height="24"
              viewBox="0 0 24 24"
              style="fill:#ffffff;">
              <path d="M 4.7070312 3.2929688 L 3.2929688 4.7070312 L 10.585938 12 L 3.2929688 19.292969 L 4.7070312 20.707031 L 12 13.414062 L 19.292969 20.707031 L 20.707031 19.292969 L 13.414062 12 L 20.707031 4.7070312 L 19.292969 3.2929688 L 12 10.585938 L 4.7070312 3.2929688 z"></path>
            </svg>
          </button>
        </div>      
      </template>
      
      <!-- template pour une tache -->
      <template v-for="block in blocks" :key="block" v-slot:[block.id]>
        <h3 class="text-lg">{{ block.title }}</h3>
        <div class="flex flex-col">
          <UpTaskButton :block="block" />
          <button class="m-auto" @click="deleteItem(block.id)"> 
            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
              width="24" height="24"
              viewBox="0 0 24 24"
              style="fill:#ffffff;">
              <path d="M 4.7070312 3.2929688 L 3.2929688 4.7070312 L 10.585938 12 L 3.2929688 19.292969 L 4.7070312 20.707031 L 12 13.414062 L 19.292969 20.707031 L 20.707031 19.292969 L 13.414062 12 L 20.707031 4.7070312 L 19.292969 3.2929688 L 12 10.585938 L 4.7070312 3.2929688 z"></path>
            </svg>
          </button>
        </div>
      </template>
    
  </kanban-board>
</div>
<AddColButton :stages="stages" @col-created="getBoard" class="" />
</div>

<div v-if="showUpColForm">
  <h2>Modifier la colonne {{ upCol.title }}</h2>
  <form>
    <label for="title">Column Title</label>
    <input  v-model="upCol.title" type="text" name="title" id="title">
    
    <button type="submit" @click="UpdateColInfo">Envoyer</button>
  </form>
  <button @click="showUpColForm = false">Close</button>
</div>

</template>

<script>
import AddTaskButton from './AddTaskButton.vue'
import AddColButton from './AddColButton.vue'
import UpTaskButton from './UpTaskButton.vue'
// import UpColButton from './UpColButton.vue'

export default {
  name : 'kanbanTable',
  components : {
    AddTaskButton,
    AddColButton,
    UpTaskButton,
    // UpColButton
  },
  data() {
    return {
      board: [],
      stages: [],
      blocks: [],
      upIndexTask: [],
      upTaskID:0,
      upTask:[],
      upCol:[],
      showUpTaskForm:false,
      showUpColForm:false,
    }
  },
  //Au chargement de la page appelle API pour GET le tableau
  created(){
    this.getBoard()
  },
  
  methods: {
    
    ShowUpdateCol(stage){
      this.upCol = stage
      this.showUpColForm = true
    },
    // Apelle API pour UPDATE le titre de la Colonne stockée dans UpCol
    async UpdateColInfo(){
      var col = {
        title:this.upCol.title,
        pos:this.upCol.pos
      }
      await fetch('http://localhost:8000/api/col/'+this.upCol.id_col+'/',{
        method:'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(col)
      });
      this.getBoard()
    },
    
    ShowUpdateTask(block){
      this.upTask = block
      this.showUpTaskForm = true
    },
    // Apelle API pour UPDATE la Tache stockée dans UpTask
    async UpdateTaskInfo(){
      var task = {
        title:this.upTask.title,
        descr:this.upTask.descr
      }
      
      await fetch('http://localhost:8000/api/task/'+this.upTask.id+'/',{
        method:'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
        
      });
      this.getBoard()
    },
    
    //Enregistrement des taches bougées lors d'un Drag & Drop
    Droped(block, list, source, sibling){
      console.log("DROPED")
      // eslint-disable-next-line
      var x = [block,source,sibling]
      // console.log(x);
      
      //Liste des taches dans le nouvelle ordre
      let taskList =list.querySelectorAll('ul > li')
      
      taskList.forEach(task => {
        this.upIndexTask.push(task.getAttribute('data-block-id'))
      })
      
    },
    
    //UPDATE d'une tache Drag & Droppé
    async updateBlock(id, status, index) {
      
      let toCol = this.board.find(t => t.title === status).id_col
      let movedTask = this.blocks.find(t => t.id == id)
      
      if(movedTask.status == status){
        for (let i = 0; i < this.upIndexTask.length; i++) {
          let tache = this.blocks.find(t => t.id == this.upIndexTask[i])
          //Cas même colonne
          if (tache.pos != i) {
            let item = {
              title:tache.title,
              descr:tache.descr,
              pos:i,
              id_col: toCol
            }
            console.log(item);
            await fetch('http://localhost:8000/api/task/'+this.upIndexTask[i]+'/',{
              method:'put',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(item) 
            });  
          }
        }
      }
      else
      {
        for (let i = index+1; i < this.upIndexTask.length; i++) {
          let tache = this.blocks.find(t => t.id == this.upIndexTask[i])
          let item = {
            title: tache.title,
            descr: tache.descr,
            pos: i,
            id_col: toCol
          }
          console.log(item);
          await fetch('http://localhost:8000/api/task/'+this.upIndexTask[i]+'/',{
            method:'put',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(item) 
          });
        }
        let item = {
          title: movedTask.title,
          descr: movedTask.descr,
          pos: index,
          id_col: toCol
        }
        await fetch('http://localhost:8000/api/task/'+id+'/',{
          method:'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(item) 
        });
      }
      this.getBoard()
      this.upIndexTask = []
    },
    
    // GET les colonnes et les taches par API
    async getBoard(){
      this.board = []
      this.stages = []
      this.blocks = []
      var response = await fetch('http://localhost:8000/api/board');
      this.board = await response.json();
      this.board.forEach((col) => {
        
        this.stages.push(col.title)
        
        col.taches.forEach(tache => {
          var item = {
            id:tache.id_task,
            status:col.title,
            title:tache.title,
            pos:tache.pos,
            descr:tache.descr
          }
          this.blocks.push(item)
        });
      });
    },
    // DELETE la colonne id
    async deleteCol(id){
      
      const col = this.stages.find(m => m.id === id);
      
      await fetch('http://localhost:8000/api/col/'+ id,{
        method:'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(col)
      });
      this.getBoard()
      
    },
    
    //DELETE la tache id
    async deleteItem(id){
      
      const task = this.blocks.find(t => t.id === id);
      
      await fetch('http://localhost:8000/api/task/'+ id,{
        method:'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
      });
      
      this.getBoard()
    }
  },
}
</script>

<style lang="scss">
@import '../assets/kanban.scss';
</style>