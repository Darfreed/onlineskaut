from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm, LoginForm
from .models import Post

def index(request):
    return render(request, '../website/index.html', {})

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

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class ChallengesView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/challenges.html"

class ForumView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/forum.html"