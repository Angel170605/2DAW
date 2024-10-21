from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasklist, name='task-list'),
    path('done/', views.done, name='done'),
    path('pending/', views.pending, name='pending'),
    path('add/', views.add, name='add'),
    path('task/<task_slug>/toggle/', views.toggle, name='toggle'),
    path('task/<task_slug>/edit/', views.edit, name='edit'),
    path('task/<task_slug>/delete/', views.delete, name='delete'),
]
