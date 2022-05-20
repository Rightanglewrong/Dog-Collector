from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

LOCATIONS = (
    ('P', 'Park'),
    ('N', 'Neighbourhood'),
    ('L', 'Lakeside')
)

class Friend(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('friends_detail', kwargs={'pk': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    friends = models.ManyToManyField(Friend)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    # Returns page to detail page of created doggo
    def get_absolute_url(self):
        return reverse('details', kwargs={'dog_id': self.id})
    


# One to Many
class Walks(models.Model):
    date = models.DateField('Walk date')
    location = models.CharField(
        max_length=1,
        choices=LOCATIONS,
        default=LOCATIONS[0][0],
        )
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
    