from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/dogs_index.html', {'dogs': dogs})

def dog_details(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog':dog})