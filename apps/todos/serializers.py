from rest_framework import serializers

from .models import Todo, Category


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'text', 'category', 'is_done', 'user']


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', ]
