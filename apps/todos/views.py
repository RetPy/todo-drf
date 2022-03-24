from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer
from .permissions import OwnerPermission


class TodoListAPIView(generics.ListAPIView):

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [OwnerPermission]


class TodoCreateAPIView(generics.CreateAPIView):

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
