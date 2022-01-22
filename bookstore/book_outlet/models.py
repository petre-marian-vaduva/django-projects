from tabnanny import verbose
from tkinter import CASCADE
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = IntegerField()


class Address(models.Model):
    street = CharField(max_length=50)
    postal_code = IntegerField()
    def __str__(self):
        return f'{self.street} {self.postal_code}'

    class Meta:
        verbose_name_plural = "Address entries"


class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Book(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
        return f'{self.name} ({self.title})'