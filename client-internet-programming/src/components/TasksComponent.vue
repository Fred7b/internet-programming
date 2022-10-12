<template>
  <div class="list row row-cols-1 row-cols-sm-1 row-cols-md-1 g-3">
    <div class="col col-sm-1 col-md-3">
      <h4>Список задач</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index === currentIndex }"
          v-for="(task, index) in tasks"
          :key="index"
          @click="setActiveTutorial(task, index)"
        >
         {{ index + 1}}: {{ task.title }}
        </li>
      </ul>

    </div>
    <div class="col-sm-1 col-md-6">
      <div v-if="currentTask">
        <h4>Задача</h4>
        <div>
          <label><strong>Заголовок:</strong></label> {{ currentTask.title }}
        </div>
        <div>
          <label><strong>Описание:</strong></label> {{ currentTask.description }}
        </div>
        <div>
          <label><strong>Статус:</strong></label> {{ currentTask.state }}
        </div>
        <div>
          <label><strong>Время создания:</strong></label> {{ currentTask.created_at }}
        </div>
        <div>
          <label><strong>Время изменения:</strong></label> {{ currentTask.last_modified }}
        </div>

        <router-link :to="'/tasks/' + currentTask.id" type="button" class="btn btn-primary">Изменить</router-link>
      </div>
      <div v-else>
        <br />
        <p>Пожалуйста выберете задачу...</p>
      </div>
    </div>
  </div>
</template>

<script>
import DataService from "../services/DataService";
export default {
  name: "task-list",
  data() {
    return {
      tasks: [],
      currentTask: null,
      currentIndex: -1,
      title: ""
    };
  },
  methods: {
    retrieveTutorials() {
      DataService.getAll()
        .then(response => {
          this.tasks = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveTutorials();
      this.currentTask = null;
      this.currentIndex = -1;
    },
    setActiveTutorial(tutorial, index) {
      this.currentTask = tutorial;
      this.currentIndex = index;
    },
  },
  mounted() {
    this.retrieveTutorials();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>