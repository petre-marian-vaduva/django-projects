from tkinter import CASCADE
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.



class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'
    

class Book(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.title})'