from django.urls import path, include
from rest_framework import routers

from task_manager import views
from task_manager.views import CreateTaskAPIView, UpdateTaskAPIView, ChangeStatusTaskAPIView, CreateProjectAPIView, \
    UpdateProjectAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tasks/', views.task_list, name='task_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('task/<int:pk>', views.task_detail, name='task_detail'),
    path('api/task/add/', CreateTaskAPIView.as_view(), name='task_api_add'),
    path('api/task/edit/<int:pk>', UpdateTaskAPIView.as_view(), name='task_api_edit'),
    path('api/task/change_status/<int:pk>',
         ChangeStatusTaskAPIView.as_view(),
         name='task_api_change_status'),

    path('api/project/add/', CreateProjectAPIView.as_view(), name='project_api_add'),
    path('api/project/edit/<int:pk>', UpdateProjectAPIView.as_view(), name='project_api_edit'),
]
