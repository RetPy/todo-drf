from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser):

    username_validator = UnicodeUsernameValidator()

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
        null=True,
        blank=True,
    )
    group = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(
        default=False,
        db_index=False,
    )
    registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'alias'

    REQUIRED_FIELDS = ['firstName', 'lastName', 'email', 'direction', 'group', 'birthday', 'age']

    def __str__(self):
        return self.alias
