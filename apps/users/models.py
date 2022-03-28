from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, email, alias, password=None, is_admin=False, is_staff=False,
                    is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not alias:
            raise ValueError("User must have a alias")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.alias = alias
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, alias, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not alias:
            raise ValueError("User must have a alias")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.alias = alias
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

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
    registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'alias'

    REQUIRED_FIELDS = ['firstName', 'lastName', 'email', 'direction', 'group', 'birthday', 'age']

    def __str__(self):
        return self.alias
