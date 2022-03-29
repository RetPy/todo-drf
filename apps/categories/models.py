from django.db import models

from apps.users.models import User


class Category(models.Model):

    title = models.CharField(
        max_length=100,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_category'
    )

    class Meta:
        unique_together = (('title', 'user'),)

    def __str__(self):
        return self.title
