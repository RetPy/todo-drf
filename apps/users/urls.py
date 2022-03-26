from django.urls import path

from .views import RegisterAPIView, UserListAPIView


urlpatterns = [
    path('all/', UserListAPIView.as_view()),
    path('register/', RegisterAPIView.as_view())
]
