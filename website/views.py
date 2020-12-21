from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .forms import RegisterForm, LoginForm
from .models import Post

def index(request):
    return render(request, '../website/index.html', {})

def profile(request):
    return render(request, '../website/profile.html', {})

def challenges(request):
    return render(request, '../website/challenges.html', {})

def forum(request):
    posts = Post.objects
    return render(request, '../website/forum.html', {})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password1')
        if form.is_valid():
            user = form.save()
            user.save()
        return redirect("/login")
    else:
        form = RegisterForm()

    return render(request, "../website/accounts/register.html", {"form":form})

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
    return render(request, '../website/accounts/login.html', {'form': form})
