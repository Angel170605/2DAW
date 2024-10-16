from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasklist, name='task-list'),
    path('tasks/', views.done, name='done'),
    path('tasks/', views.pending, name='pending'),
    path('tasks/', views.add, name='add'),
    path('tasks/g/<task_slug>/', views.toggle, name='toggle'),
    path('tasks/g/<task_slug>/', views.edit, name='edit'),
    path('tasks/g/<task_slug>/', views.delete, name='delete'),
]
