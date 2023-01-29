from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics, response, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from apps.todos.models import Category
from apps.users.serializers import UserSerializer, LoginSerializer

User = get_user_model()


class UserRegisterAPIView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer

    def perform_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Category.objects.create(name='Без категории', user=serializer.instance)
        return response.Response(serializer.data)


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({
            'token': token.key,
        })


class UserLogoutView(APIView):
    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return response.Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
