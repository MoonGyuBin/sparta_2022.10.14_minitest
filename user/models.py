from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    phonenum = models.CharField(max_length = 12)
    adress = models.CharField(max_length=50)