from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import MyUserManager


class User(AbstractUser):
    user = None
    alias = models.CharField(
        max_length=255,
        unique=True,
    )
    firstName = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    lastName = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )
    registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'alias'

    objects = MyUserManager()

    def __str__(self):
        return self.alias
