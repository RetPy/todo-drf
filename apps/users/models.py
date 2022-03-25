from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class User(AbstractUser):

    DIR_CHOICES = (
        ('1', 'Android'),
        ('2', 'Backend'),
        ('3', 'Frontend'),
    )
    alias = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
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
    direction = models.CharField(
        max_length=15,
        choices=DIR_CHOICES,
    )
    group = models.CharField(
        max_length=50
    )
    birthday = models.DateField(
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    REQUIRED_FIELDS = ['alias', 'firstName', 'lastName', 'email', 'direction', 'group', 'birthday', 'age']

    def __str__(self):
        return self.alias
