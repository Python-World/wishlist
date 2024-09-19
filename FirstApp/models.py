from django.db import models

class Wish(models.Model):
    wishtitle = models.CharField(max_length=200)
    mywish = models.TextField()
    deadline = models.DateField(blank=True, null=True)  # Make deadline optional

    def __str__(self):
        return self.wishtitle
