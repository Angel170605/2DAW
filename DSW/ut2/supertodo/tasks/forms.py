from django import forms

from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'complete_before': forms.DateInput(attrs={'type': 'date'}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'complete_before': forms.DateInput(attrs={'type': 'date'}),
        }
