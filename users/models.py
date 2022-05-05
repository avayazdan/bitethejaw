from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  

    submissions = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=50, default=None)
    bio = models.CharField(max_length=300, default="Add your bio here")
    display_picture = models.CharField(max_length=200, default="Add a display picture here")
    

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.username}"
      