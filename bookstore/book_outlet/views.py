from django.shortcuts import render
from .models import Family
# Create your views here.

def index(request):
    members = Family.objects.all()
    return render(request, 'book_outlet/index.html', {
        'members': members
    })