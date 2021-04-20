from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT

# Create your models here.

class CustomUser(AbstractUser):
    projects = models.ManyToManyField('projects.Project', blank=True)
