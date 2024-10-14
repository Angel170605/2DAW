from django.contrib import admin

from .models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    repopulated_fields = {'slug': ['title']}
