
from django.db import models


class Submissions(models.Model):
    """
    User submissons
    """
    image = models.CharField(max_length=50, default=None)
    submitted_by = models.CharField(max_length=50, default=None)
    date_submitted = models.DateField(default=None)
    text_field = models.CharField(max_length=2000, default=None)
    category = models.CharField(max_length=50, default=None)

def __str__(self):
    """Formats entries in the Admin panel"""
    return f"{self.text_field} - {self.image}"
