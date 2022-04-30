
from sre_parse import CATEGORIES
from django.db import models

CATEGORIES = [
    ('at', "Art"),
    ('hi', "History"),
    ('ph', "Philosophy"),
    ('po', "Politics"),
    ('pm', "Poetry"),
    ('ms', "Misc")
]


class Submissions(models.Model):
    """
    User submissons
    """
    image = models.CharField(max_length=200, default=None)
    submitted_by = models.CharField(max_length=50, default=None)
    date_submitted = models.DateField(default=None)
    text_field = models.CharField(max_length=2000, default=None)
    category = models.TextField(
        choices=CATEGORIES,
        default=None,
    )


def __str__(self):
    """Formats entries in the Admin panel"""
    return f"{self.text_field} - {self.image}"
