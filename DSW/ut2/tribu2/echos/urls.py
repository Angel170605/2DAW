from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echos, name='echos'),
    path('/<id>/', views.detail, 'detail'),
    path('/<id>/edit/', views.edit, name='edit'),
    path('/<id>/delete', views.delete, name='delete'),
]
