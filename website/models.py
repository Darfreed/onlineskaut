from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    autor = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="post")
    nazev = models.CharField(max_length=60)
    text = models.TextField()
    vyzva = models.BooleanField("vyzva")
    datum = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nazev

class UserProfile(models.Model):
    nickname = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    

    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname