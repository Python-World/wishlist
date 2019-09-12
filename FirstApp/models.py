from django.db import models

# Create your models here.
class Wish(models.Model):
    wishtitle=models.CharField(max_length=250)
    mywish=models.CharField(max_length=1000)
    def __str__(self):
        return  self.wishtitle