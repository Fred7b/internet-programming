from django.urls import path, include

from task_manager import views
from task_manager.views import CreateTaskAPIView, UpdateTaskAPIView, ChangeStatusTaskAPIView, CreateProjectAPIView, \
    UpdateProjectAPIView, TaskAPIView, TaskDetailAPIView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/task/', TaskAPIView.as_view(), name='task_api_get'),
    path('api/task/<int:id>', TaskDetailAPIView.as_view(), name='task_api_get_detail'),
    path('api/task/add/', CreateTaskAPIView.as_view(), name='task_api_add'),
    path('api/task/edit/<int:id>', UpdateTaskAPIView.as_view(), name='task_api_edit'),
    path('api/task/change_status/<int:id>',
         ChangeStatusTaskAPIView.as_view(),
         name='task_api_change_status'),

    path('api/project/add/', CreateProjectAPIView.as_view(), name='project_api_add'),
    path('api/project/edit/<int:id>', UpdateProjectAPIView.as_view(), name='project_api_edit'),
]
