from django.urls import path

from apps.users.views import *


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
