from django.conf.urls import url
from . import views


urlpatterns = [
     url('^$', views.index, name='index'),
     url('profile', views.profile, name='profile'),
     url('challenges', views.challenges, name='challenges'),
     url('forum', views.forum, name='forum'),

     #Django Auth
     url('register', views.register, name='register'),
     url('login', views.loginin, name='login'),
]