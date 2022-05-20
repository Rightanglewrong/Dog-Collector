from django.shortcuts import redirect, render
from .forms import WalksForm
from .models import Dog, Friend
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/dogs_index.html', {'dogs': dogs})


@login_required
def dog_details(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    friends_dog_dont_have = Friend.objects.exclude(
        id__in=dog.friends.all().values_list('id'))
    walks_form = WalksForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'walks_form': walks_form,
        'friends': friends_dog_dont_have
    })


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    # fields = '__all__' OR
    fields = ['name', 'breed', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # success_url = '/cats/' if absolute url method isnt used


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'


@login_required
def add_walk(request, dog_id):
    form = WalksForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.dog_id = dog_id
        new_walk.save()
    return redirect('details', dog_id=dog_id)


def assoc_friend(request, dog_id, friend_id):
    Dog.objects.get(id=dog_id).friends.add(friend_id)
    return redirect('details', dog_id=dog_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
        # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class FriendList(LoginRequiredMixin, ListView):
    model = Friend


class FriendDetail(LoginRequiredMixin, DetailView):
    model = Friend


class FriendCreate(LoginRequiredMixin, CreateView):
    model = Friend
    fields = '__all__'


class FriendUpdate(LoginRequiredMixin, UpdateView):
    model = Friend
    fields = ['name']


class FriendDelete(LoginRequiredMixin, DeleteView):
    model = Friend
    success_url = '/friends/'
