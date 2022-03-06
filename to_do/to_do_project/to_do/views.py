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

def update(request, number):
    row = Task.objects.get(pk=number)
    form = TaskForm(instance=row)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'to_do/update.html', {
        'form': form
    })

def delete(request, number):
    task = Task.objects.get(id=number)

    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect('/')

    return render(request, 'to_do/delete.html', {
        'task': task
    })