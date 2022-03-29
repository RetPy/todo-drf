from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from apps.categories.models import Category


class UserListAPIView(generics.ListAPIView):
    """
    tmp view of Users List
    """

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    User registration view
    """

    model = User
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Category.objects.create(title='Без категории', user=serializer.instance)
        return Response(serializer.data)
