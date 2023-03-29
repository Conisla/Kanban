<template>
    <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock"></kanban-board>
</template>
  
  <script>
  export default {
    name : 'kanbanTable',
    data() {
    return {
      stages: ["todo", "in-progress", "needs-review", "approved"],
      blocks: [
      {
        id: 0,
        status: "approved",
        title: "Buy coffee machine"
      },
      {
        id: 1,
        status: "in-progress",
        title: "Find better AirBnB options"
      },
      {
        id: 2,
        status: "todo",
        title: "AirBnB options",
        
      },
      ]
    }
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
  },
}
</script>

<style lang="scss">
@import "../assets/kanban.scss"
</style>