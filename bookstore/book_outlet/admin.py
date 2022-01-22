from atexit import register
from os import name
from django.contrib import admin
from .models import Book, Name
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


class NameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
admin.site.register(Name, NameAdmin)