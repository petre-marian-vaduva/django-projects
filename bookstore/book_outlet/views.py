from turtle import title
from django.shortcuts import render
from .models import Book, Name
# Create your views here.

def index(request):
    books = Book.objects.all()
    authors = Name.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books
    })