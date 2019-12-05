from django.db import models
from django import forms

# Create your models here.
from django import forms


class Addition(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        info = str(self.name) + str(self.email) + str(self.password)
        return info
