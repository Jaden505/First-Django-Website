from . import models
from django import forms

class CreateTodo(forms.ModelForm):
    class Meta:
        model = models.Addition
        fields = ['name_todo', 'description_todo', 'deadline_todo', 'email_notification']
