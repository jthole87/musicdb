from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import PROTECT
# Create your models here.

class Project(models.Model):
    created_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])