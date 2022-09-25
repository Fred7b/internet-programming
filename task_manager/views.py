from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView

from task_manager.models import Task, Project
from task_manager.serializers import CreateTaskSerializer, UpdateTaskSerializer, ChangeStatusTaskSerializer, \
    CreateProjectSerializer, UpdateProjectSerializer
from task_manager.services import servises


class CreateTaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer

    def perform_create(self, serializer):
        # pass
        serializer.save(created_by=self.request.user,
                        created_at=timezone.now())


class UpdateTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())


class CreateProjectAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer

    def perform_create(self, serializer):
        # pass
        serializer.save(created_at=timezone.now())


class UpdateProjectAPIView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = UpdateProjectSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())

class ChangeStatusTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = ChangeStatusTaskSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())


def task_list(request):
    tasks = servises.get_tasks(request)
    data = {'tasks': tasks}
    return render(request, 'task_list.html', data)


def task_detail(request, pk):
    task = servises.get_task_by_pk(pk)
    data = {'task': task}
    return render(request, 'task_detail.html', data)
