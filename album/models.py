from django.db import models
from django.utils import timezone
from musician.models import MusicianModel
# Create your models here.

CHOICES = (("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),)

class AlbumModel(models.Model):
    album_name = models.CharField(max_length = 50)
    rating = models.CharField(max_length = 1,choices = CHOICES,default = '1')
    release_date = models.DateField(default = timezone.now)
    musician = models.ForeignKey(MusicianModel,on_delete = models.CASCADE)