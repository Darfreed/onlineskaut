from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nazev = models.CharField(max_length=60)
    text = models.TextField()
    vyzva = models.BooleanField("vyzva")
    datum = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nazev
