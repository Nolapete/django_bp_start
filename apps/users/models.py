from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extends the default AbstractUser to create a custom user model.
    """

    # By inheriting from AbstractUser, we get all the default fields
    # (username, password, email, first_name, last_name, etc.)

    # You can add custom fields here if needed.
    # For example:
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

