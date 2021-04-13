from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth import get_user_model


# Create your models here.

class Song(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=PROTECT)
    title = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    project = models.ForeignKey('projects.Project', on_delete=PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])

