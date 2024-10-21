from django.contrib import admin

from .models import Task


@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'slug',
        'done',
        'completed_before',
        'created_at',
        'updated_ad',
    ]
    repopulated_fields = {'slug': ['title']}
