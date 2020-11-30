from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('addPost/', views.addPost, name='addPost'),
    path('myPost/', views.myPost, name='myPost'),
    path('ParticularPost/<int:id>/', views.ParticularPost, name='ParticularPost'),
path('share/', views.share, name='share'),

]
