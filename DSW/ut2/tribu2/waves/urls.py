from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('', views.waves, name='echos'),
]
