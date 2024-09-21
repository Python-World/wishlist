from django.db import models

class Wish(models.Model):
    wishtitle = models.CharField(max_length=200)  # Title of the wish
    mywish = models.TextField()  # Detailed description of the wish
    deadline = models.DateField(blank=True, null=True)  # Optional field for the wish's deadline

    def __str__(self):
        return self.wishtitle  # Displays the title in the Django admin or shell
