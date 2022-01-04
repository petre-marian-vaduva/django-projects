from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    my_rating = models.IntegerField()

class pets(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Family(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(MinLengthValidator(1), MaxLengthValidator(5)) 


    def __str__(self):
        return f'{self.name} ({self.age})'
    
    