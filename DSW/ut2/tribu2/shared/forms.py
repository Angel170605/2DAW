from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = dict(password=forms.PasswordInput)
