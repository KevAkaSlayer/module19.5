from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length  = 100)
    email = models.EmailField()
    PhoneNo = models.CharField(max_length = 12)
    InstruType = models.CharField(max_length = 14)


    def __str__(self):
        return  self.first_name