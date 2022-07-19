from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=25)

