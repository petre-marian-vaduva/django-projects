from dataclasses import fields
from to_do.models import Task
from django.forms import ModelForm
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']
        labels = {
            'title': 'Your title',
            'complete': 'Is it completed ?'
        }