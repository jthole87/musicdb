from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
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

class SongStructure(models.Model):
    song = models.ForeignKey(Song, on_delete=CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{} structure'.format(self.song.title)

class StructurePart(models.Model):
    stucture = models.ForeignKey('songs.SongStructure', on_delete=CASCADE)
    part_type = models.CharField(max_length=25)
    length = models.PositiveSmallIntegerField()
    start = models.PositiveSmallIntegerField(blank=True,null=True)
    position = models.PositiveSmallIntegerField(blank=True,null=True) # TODO: Figure out how to make this unique per each structure

