from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from to_do.forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request, 'to_do/index.html', {
        'form': form,
        'tasks': tasks
    })

def test(request, number):
    row = Task.objects.get(pk=number)
    form = TaskForm(instance=row)
    return render(request, 'to_do/test.html', {
        'form': form
    })