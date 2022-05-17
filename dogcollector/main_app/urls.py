from django.urls import path
# From this file level, imports the views.py
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('dogs/', views.dogs_index, name = 'dogs'),
    path('dogs/<int:dog_id>/', views.dog_details, name = 'details'),
]