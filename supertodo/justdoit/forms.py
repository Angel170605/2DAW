from django import forms

from .models import ToDo


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('name', 'description')
