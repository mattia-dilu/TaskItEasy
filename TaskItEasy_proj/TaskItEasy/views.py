from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import  reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistrationForm

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "TaskItEasy/index.html", {
            "message": "Invalid credentials."
            })
    return render(request, "TaskItEasy/index.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'TaskItEasy/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index') 

def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('index')
    else:
        return render(request, 'TaskItEasy/delete_user.html')
                    

@login_required
def home(request):
    return render(request, 'TaskItEasy/home.html')