from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echos, name='echos'),
    path('add/', views.add_echo, name='add'),
    path('<echo_id>/detail/', views.detail, name='detail'),
    path('<echo_id>/edit/', views.edit, name='edit'),
    path('<echo_id>/delete/', views.delete, name='delete'),
]
