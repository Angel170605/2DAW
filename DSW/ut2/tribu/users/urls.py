from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('<user_id>/echos', views.user_echos, name='user_echos'),
]
