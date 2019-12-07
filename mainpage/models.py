from django.db import models
from django import forms

# Create your models here.
from django import forms


class Addition(models.Model):
    name_todo = models.CharField(max_length=100)
    description_todo = models.TextField(blank=True)
    deadline_todo = models.DateTimeField()
    email_notification = models.BooleanField()

    def __str__(self):
        info = str(self.name_todo) + str(self.description_todo) + str(self.deadline_todo)
        return info
