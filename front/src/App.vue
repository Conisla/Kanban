<template>
    <AddTaskButton :blocks="blocks" :board="board"/>
    <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock" @updating="updateTaskInfo"></kanban-board>
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
            showUpTaskForm:false
        }
    },
     async created(){
      await this.getBoard()
      console.log(this.board);
    },

  methods: {
    async updateTaskInfo(id){
      console.log(id);
      this.showUpTaskForm = true
    },

    async updateBlock(id, status, index) {
      console.log("=====================");
      console.log("id_task = ",this.blocks.find(b => b.id === Number(id)).id );
      console.log("old status =",this.blocks.find(b => b.id === Number(id)).status );

      var tache = this.blocks.find(b => b.id === Number(id)) 
      tache.status = status;

      console.log("id_col =",this.board.find(t => t.title == status).id_col);
      console.log("tache =",tache);
      var item = {
        title:tache.title,
        descr:tache.descr,
        pos:index,
        id_col:this.board.find(t => t.title == status).id_col
      }

      console.log("new status =",this.blocks.find(b => b.id === Number(id)).status );

      console.log("index =", index );
      console.log("=====================");

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