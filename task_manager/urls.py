from django.template.defaulttags import url
from django.urls import path

from task_manager import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/', views.task_detail, name='task_detail'),
    path('task_create/', views.task_create, name='task_detail'),
    path('task_update/', views.task_update, name='task_detail'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
