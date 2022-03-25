from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer
from .permissions import OwnerPermission


class TodoListAPIView(generics.ListAPIView):

    """
    Show all todos
    """

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [OwnerPermission, IsAuthenticated]


class TodoCreateAPIView(generics.CreateAPIView):

    """
    Create new todos
    """

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [OwnerPermission, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
