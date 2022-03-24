from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Todo
        fields = ['title', 'text', 'user']
