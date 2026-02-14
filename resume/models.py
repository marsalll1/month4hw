from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    about_me = models.TextField()

    def __str__(self):
        return self.user.username

