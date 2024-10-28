from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echos, name='echos'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]
