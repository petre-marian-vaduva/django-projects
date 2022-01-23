from email import charset
from sre_constants import SRE_INFO_LITERAL
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from datetime import datetime
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')
    title = models.CharField(max_length=50)
    Excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)

