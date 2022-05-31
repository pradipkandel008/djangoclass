from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='static/uploads', default='static/default_user.png')
    address = models.CharField(max_length=200)
    bio = models.TextField(max_length=5000)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
