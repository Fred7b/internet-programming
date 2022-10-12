<template>
  <div>
    <div v-if="currentTask" class="edit-form">
      <h4>Задача</h4>
      <form>
        <div class="form-group">
          <label for="title">Заголовок</label>
          <input type="text" class="form-control" id="title"
            v-model="currentTask.title"
          />
        </div>
        <div class="form-group">
          <label for="description">Описание</label>
          <input type="text" class="form-control" id="description"
            v-model="currentTask.description"
          />
        </div>
        <div class="form-group">
          <label for="state">Статус</label>
          <input type="text" class="form-control" id="state"
            v-model="currentTask.state"
          />
        </div>
      </form>
      <button type="submit" class="btn btn-primary"
        @click="updateTask"
      >
        Обновить
      </button>
      <p>{{ message }}</p>
    </div>

    <div v-else>
      <br />
      <p>Нажмите на задачу...</p>
    </div>
  </div>
</template>

<script>
import DataService from "../services/DataService";
export default {
    name: "task-details",
    data() {
      return {
        currentTask: null,
        message: ''
      };
    },
    methods: {
      getTask(id) {
        DataService.get(id)
          .then(response => {
            this.currentTask = response.data;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },
      updatePublished(status) {
        let data = {
          id: this.currentTask.id,
          title: this.currentTask.title,
          description: this.currentTask.description,
          published: status
        };
        DataService.update(this.currentTask.id, data)
          .then(response => {
            this.currentTask.published = status;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },
      updateTask() {
        let data = {
          'title': this.currentTask.title,
          'description': this.currentTask.description,
        };
        DataService.update(this.currentTask.id, data)
          .then(response => {
            console.log(response.data);
            this.message = 'The tutorial was updated successfully!';
          })
          .catch(e => {
            console.log(e);
          });
      },
    },
    mounted() {
      this.message = '';
      this.getTask(this.$route.params.id);
    }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>