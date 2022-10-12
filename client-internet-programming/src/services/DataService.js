import http from "../http-client-common";

class TaskDataService {
  getAll() {
    return http.get("/task/?format=json");
  }

  get(id) {
    return http.get(`/task/${id}`);
  }

  create(data) {
    return http.post("/task/add/", data);
  }

  update(id, data) {
    return http.put(`/task/edit/${id}`, data);
  }

  delete(id) {
    return http.delete(`/tasks/${id}`);
  }

}

export default new TaskDataService();