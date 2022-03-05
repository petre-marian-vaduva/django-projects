from django.http import HttpResponse
from django.shortcuts import render
from to_do.forms import TaskForm

# Create your views here.

def index(request):
    form = TaskForm()
    return render(request, 'to_do/index.html', {
        'form': form
    })

def test(request):
    return render(request, 'to_do/test.html')