from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_user/', views.delete_user, name='delete_user'),
]       