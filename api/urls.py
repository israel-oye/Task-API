from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.task_list),

    path('tasks', views.create_task),
    path('task/<pk>', views.task_detail),
]