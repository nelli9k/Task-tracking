from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_to', 'status', 'assigned_to']

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(choices=[
        ('all', 'All'),
        ('todo', 'To do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], required=False)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label = "Confirm password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password and password_confirmation and password !=  password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data