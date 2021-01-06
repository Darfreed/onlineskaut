from django.shortcuts import render, redirect  
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm 

def index(request: HttpRequest) -> HttpResponse:
    return render(request, '../website/index.html', {})

def register(request: HttpRequest) -> HttpResponse:
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