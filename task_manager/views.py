# Create your views here.
from django.utils import timezone
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from task_manager.models import Task, Project
from task_manager.serializers import CreateTaskSerializer, UpdateTaskSerializer, ChangeStatusTaskSerializer, \
    CreateProjectSerializer, UpdateProjectSerializer, TaskSerializer


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_at=timezone.now())


class UpdateTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())


class CreateProjectAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=timezone.now())


class UpdateProjectAPIView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = UpdateProjectSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())


class ChangeStatusTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = ChangeStatusTaskSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(last_modified=timezone.now())
