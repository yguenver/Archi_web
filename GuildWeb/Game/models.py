import datetime

from django.db import models
from django.utils import timezone
from django.views.generic import TemplateView

from django.contrib.auth.models import UserManager, AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()
