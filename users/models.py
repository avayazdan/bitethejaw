from django.db import models


class User(models.Model):  

    username = models.CharField(max_length=50)
    submissions = models.CharField(max_length=50)
    data_joined = models.DateField

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.name} - {self.branch}"
      