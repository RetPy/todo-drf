from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    DIR_CHOICES = (
        ('A', 'Android'),
        ('B', 'Backend'),
        ('F', 'Frontend'),
    )
    username = models.CharField(
        max_length=100,
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

    REQUIRED_FIELDS = ['firstName', 'lastName', 'email', 'direction', 'group', 'birthday', 'age']

    def __str__(self):
        return self.username
