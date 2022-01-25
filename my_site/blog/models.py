from email import charset
from email.policy import default
from logging import captureWarnings
from sre_constants import SRE_INFO_LITERAL
from tkinter import CASCADE
from django.db import models
from django.forms import CharField, SlugField
from datetime import datetime
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.email_address}'

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=50)
    Excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField()


