from audioop import reverse
from turtle import title
from django.shortcuts import render
from .models import Book, Name
from django.http import HttpResponseRedirect
from .forms import ReviewForm


def index(request): 
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        print(review_form.cleaned_data)
        return HttpResponseRedirect('/book_detail.html')

    return render(request, 'book_outlet/index.html', {
        'review_form': review_form
    })


def book_detail(request):
    return render(request, 'book_outlet/book_detail.html')