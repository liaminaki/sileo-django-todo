from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    
    class Meta:
        model = Todo
        fields = ['label', 'done', 'todo_uuid']

