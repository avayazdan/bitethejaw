from django.db import models


class User(models.Model):  

    username = models.CharField(max_length=50)
    submissions = models.CharField(max_length=50)
    date_joined = models.DateField
    email = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)


    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.username}"
      