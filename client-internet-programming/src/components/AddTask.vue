<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="title">Заголовок</label>
        <input
          type="text"
          class="form-control"
          id="title"
          required
          v-model="task.title"
          name="title"
        />
      </div>
      <div class="form-group">
        <label for="description">Описание</label>
        <textarea
          class="form-control"
          id="description"
          required
          v-model="task.description"
          name="description"
        />
      </div>

      <button @click="saveTutorial" class="btn btn-success">Добавить задачу</button>
    </div>

    <div v-else>
      <h4>Вы успешно создали задачу</h4>
      <button class="btn btn-success" @click="newTutorial">Добавить новую задачу</button>
    </div>
  </div>
</template>

<script>
import DataService from "../services/DataService";
export default {
  name: "add-task",
  data() {
    return {
      task: {
        id: null,
        title: "",
        description: "",
        // published: false
      },
      submitted: false
    };
  },
  methods: {
    saveTutorial() {
      let data = {
        'title': this.task.title,
        'description': this.task.description
      };
      DataService.create(data)
        .then(response => {
          this.task.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },

    newTutorial() {
      this.submitted = false;
      this.task = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>