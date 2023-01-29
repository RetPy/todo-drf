from rest_framework.viewsets import ModelViewSet

from apps.todos.models import Todo, Category
from apps.todos.serializers import TodoSerializer, CategorySerializer
from apps.todos.permissions import OwnerPermission


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    filterset_fields = ['category', 'created_date', 'is_done']
    search_field = ['title']
    permission_classes = [OwnerPermission]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    search_field = ['title']

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
