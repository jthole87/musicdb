from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth import get_user_model


# Create your models here.
class Recording(models.Model):
    def upload_path(self):
        project = self.song.project
        title = self.song.title
        return ('{}/{}/'.format(project, title))

    author = models.ForeignKey(get_user_model(), on_delete=PROTECT)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=80000, blank=True, null=True)
    recording = models.FileField(upload_to=upload_path)
    song = models.ForeignKey('songs.Song', on_delete=PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recording_detail', args=[str(self.id)])