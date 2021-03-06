from django.db import models

from apps.users.models import User
from apps.categories.models import Category


class Todo(models.Model):

    title = models.CharField(
        max_length=255
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    is_done = models.BooleanField(
        default=False,
        db_index=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_todo'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_todo'
    )

    def __str__(self):
        return self.title
