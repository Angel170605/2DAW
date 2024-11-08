from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('', views.waves, name='echos'),
    path('add/<echo_id>/', views.add_wave, name='add'),
    path('<echo_id>/<wave_id>/edit/', views.edit, name='edit'),
    path('<echo_id>/<wave_id>/delete/', views.delete, name='delete'),
]
