from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, '../onlineskaut_website/index.html', {})

def profile(request):
    return render(request, '../onlineskaut_website/profile.html', {})

def challenges(request):
    return render(request, '../onlineskaut_website/challenges.html', {})

def forum(request):
    return render(request, '../onlineskaut_website/forum.html', {})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "../onlineskaut_website/accounts/register.html", {"form":form})

def loginin(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password')
        if form.is_valid:
            user = authenticate(username=name, password=passw)
            login(request, user)
            return redirect('/profile')
    else:
        form = LoginForm()
    return render(request, '../onlineskaut_website/accounts/login.html', {'form': form})