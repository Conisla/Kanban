<template>
    <AddTaskButton :blocks="blocks" :board="board"/>
    <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock" @updating="ShowUpdateTask"></kanban-board>
    <div v-if="showUpTaskForm">
        <form>
            <label for="title">Task Title</label>
            <input  v-model="upTitle" type="text" name="title" id="title">

            <label for="descr">Task Description</label>
            <input  v-model="upDescr" type="text" name="descr" id="descr">

            <button type="submit" @click="UpdateTaskInfo()">Envoyer</button>
        </form>
        <button @click="showUpTaskForm = false">Close</button>
    </div>

    <AddColButton :stages="stages"/>
</template>

<script>
  import AddTaskButton from './components/AddTaskButton.vue'
  import AddColButton from './components/AddColButton.vue'

export default {
  name : 'App',
  components : {
    AddTaskButton,
    AddColButton
  },
  data() {
        return {
            board: [],
            stages: [],
            blocks: [],
            toUpdate:0,
            upTitle:'',
            upDescr:'',
            item:{
              "title": "",
              "descr": "",
              "pos": 0,
              "id_col": 0
            },
            showUpTaskForm:false
        }
    },
     async created(){
      await this.getBoard()
      console.log(this.board);
    },

  methods: {
    ShowUpdateTask(id){
      this.toUpdate = id
      this.showUpTaskForm = true
      let el = this.blocks.find(t => t.id == this.toUpdate)

      let taches = this.board.find(e => e.title == el.status).taches

      let index = taches.find(t => t.id_task == this.toUpdate).pos

      this.item = {
        title: el.title,
        descr: el.descr,
        pos: index,
        id_col: Number(this.board.find(t => t.title == el.status).id_col)
      }
    },
  
    async UpdateTaskInfo(){
      this.item.title = this.upTitle
      this.item.descr = this.upDescr
      
      await fetch('http://localhost:8000/api/task/'+this.toUpdate+'/',{
        method:'put',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.item)
        
      });
    },

    async updateBlock(id, status, index) {

      var tache = this.blocks.find(b => b.id === Number(id)) 

      var item = {
        title:tache.title,
        descr:tache.descr,
        pos:index,
        id_col:this.board.find(t => t.title == status).id_col
      }

      await fetch('http://localhost:8000/api/task/'+id+'/',{
        method:'put',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(item)
        
      });

    },

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
                    descr:tache.descr
                }
                this.blocks.push(item)
            });
      });
    },

    async deleteCol(id){

      const col = this.stages.find(m => m.id === id);

      await fetch('http://localhost:8000/api/col/'+ id,{
          method:'delete',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(col)
      });
      await this.getBoard()
    }
  },
}
</script>

<style lang="scss">
@import "./assets/kanban.scss"
</style>