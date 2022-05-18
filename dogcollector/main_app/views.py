from tkinter import W
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import WalksForm
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    walks_form = WalksForm()
    return render(request, 'dogs/detail.html', {'dog':dog, 'walks_form': walks_form})

class DogCreate(CreateView):
    model= Dog
    fields= '__all__'
    # Or fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' if absolute url method isnt used
    
class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url= '/dogs/'

def add_walk(request, dog_id):
    form = WalksForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.dog_id = dog_id
        new_walk.save()
    return redirect('details', dog_id= dog_id)