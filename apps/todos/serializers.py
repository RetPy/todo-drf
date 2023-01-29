from rest_framework import serializers

from apps.todos.models import Todo, Category


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,
    )

    class Meta:
        model = Todo
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,
    )

    class Meta:
        model = Category
        fields = '__all__'
