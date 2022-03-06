from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<number>', views.update, name='update'),
    path('delete/<number>', views.delete, name='delete'),
]