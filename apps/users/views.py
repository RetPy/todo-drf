from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class RegisterAPIView(generics.CreateAPIView):

    model = User
    serializer_class = UserSerializer
