from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .models import Todo
from .serializers import TodoSerializer
from .permissions import OwnerPermission


class TodoListAPIView(generics.ListAPIView):

    """
    Show all todos
    """

    model = Todo
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'created_date', 'is_done']
    permission_classes = [OwnerPermission]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


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


class TodoDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):

    model = Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [OwnerPermission, IsAuthenticated]
