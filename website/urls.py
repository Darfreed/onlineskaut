from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url("^$", views.index, name="index"),
    url("accounts/profile", views.ProfileView.as_view(), name="profile"),
    url("accounts/challenges", views.ChallengesView.as_view(), name="challenges"),
    url("accounts/forum", views.ForumView.as_view(), name="forum"),
    # Django Auth
    url("register", views.register, name="register"),
    path(
        "accounts/login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
