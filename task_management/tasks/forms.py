from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Назначить пользователю")

    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to']
