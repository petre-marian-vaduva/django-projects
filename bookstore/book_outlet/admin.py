from atexit import register
from os import name
from django.contrib import admin
from .models import Address, Book, Country, Name
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')



admin.site.register(Country)
admin.site.register(Address)