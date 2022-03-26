from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPIView(generics.CreateAPIView):

    model = User
    serializer_class = UserSerializer
