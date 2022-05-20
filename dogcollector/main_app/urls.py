from django.urls import path
# From this file level, imports the views.py
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('dogs/', views.dogs_index, name = 'dogs_index'),
    path('dogs/<int:dog_id>/', views.dog_details, name = 'details'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name='dog_update'),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name ='dog_delete'),
    path('dogs/<int:dog_id>/add_walk', views.add_walk, name='add_walk'),
    path('dogs/<int:dog_id>/assoc_friend/<int:friend_id>/', views.assoc_friend, name='assoc_friend'),
    # Friend Route
    path('friends/', views.FriendList.as_view(), name='friends_index'),
    path('friends/<int:pk>/', views.FriendDetail.as_view(), name='friends_detail'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name ='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name ='friends_delete'),
    # Auth Routes
    path('accounts/signup/', views.signup, name='signup'),
]
# CBVs working w/ individual model instances expect to find a named parameter of pk. 
# This is why we didn't use cat_id as we did in the detail entry.