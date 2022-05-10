from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    date_joined = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=50, default=None)
    bio = models.CharField(max_length=1000, default="Add your bio here")
    display_picture = models.CharField(
        max_length=200, blank=True, default="This user doesn't have a display picture")

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.username}"
