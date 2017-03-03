import datetime

from django.db import models
from django.utils import timezone
from django.views.generic import TemplateView


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)