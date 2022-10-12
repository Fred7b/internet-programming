from rest_framework import serializers

from task_manager.models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['last_modified', 'created_at', 'created_by']


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['last_modified', 'created_at', 'created_by']


class ChangeStatusTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['state']


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['last_modified', 'created_at', 'created_by']


class UpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['last_modified', 'created_at', 'created_by']
