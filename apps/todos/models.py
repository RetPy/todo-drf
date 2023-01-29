from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=255,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='category_user',
    )

    class Meta:
        unique_together = (('title', 'user',),)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    is_done = models.BooleanField(
        default=False,
        db_index=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='todo_category',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todo_user',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title
