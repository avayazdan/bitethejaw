# import uuid
from sre_parse import CATEGORIES
from django.conf import settings
from django.db import models
from users.models import User

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
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # submission_id = models.PositiveIntegerField(primary_key=True)
    # uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    image = models.CharField(max_length=200, default=None)
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # submitted_by = models.ForeignKey(
    #     User, related_name="submitted_by", on_delete=models.PROTECT)
    date_submitted = models.DateField(auto_now_add=True)
    text_field = models.CharField(max_length=2000, default=None)
    category = models.TextField(
        choices=CATEGORIES,
        default=None,
    )

    # def utcoffset(self, dt):
    #     return self.__offet

    def __str__(self):
        """Formats entries in the Admin panel"""
        return f"{self.text_field} - {self.image}"
