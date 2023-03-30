<template>
    <AddTaskButton/>
    <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock"></kanban-board>
    <AddColButton/>
    <button @click="deleteCol(18)">del col 3</button>
</template>
  
  <script>
  import AddTaskButton from 'AddTaskButton.vue'
  import AddColButton from 'AddColButton.vue'

  export default {
    name : 'kanbanTable',
    components: {
      AddTaskButton,
      AddColButton
    },
    data() {
        return {
            board: [],
            stages: [],
            blocks: []
        }
    },
     async created(){
      await this.getBoard()
      console.log(this.board);
    },

  methods: {
    updateBlock(id, status, index) {
      console.log("=====================");
      console.log("id = ",this.blocks.find(b => b.id === Number(id)).id );
      console.log("old status =",this.blocks.find(b => b.id === Number(id)).status );

      this.blocks.find(b => b.id === Number(id)).status = status;

      console.log("new status =",this.blocks.find(b => b.id === Number(id)).status );
      console.log("index =", index );
      console.log("=====================");
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
                    title:tache.title
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
@import "../assets/kanban.scss"
</style>