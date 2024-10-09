from django.urls import path

from . import views

app_name = 'justdoit'

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/<task_slug>/', views.task_detail, name='task_detail'),
]
