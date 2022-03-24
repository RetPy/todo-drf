from django.urls import path

from .views import TodoListAPIView, TodoCreateAPIView


urlpatterns = [
    path('all/', TodoListAPIView.as_view()),
    path('create/', TodoCreateAPIView.as_view())
]
