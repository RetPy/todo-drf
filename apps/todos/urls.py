from django.urls import path

from .views import TodoListAPIView, TodoCreateAPIView, TodoDetailUpdateDeleteAPIView


urlpatterns = [
    path('all/', TodoListAPIView.as_view()),
    path('create/', TodoCreateAPIView.as_view()),
    path('detail/<int:pk>/', TodoDetailUpdateDeleteAPIView.as_view()),
]
