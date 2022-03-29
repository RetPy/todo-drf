from django.urls import path

from .views import *


urlpatterns = [
    path('', CategoryListAPIView.as_view()),
    path('create/', CategoryCreateAPIView.as_view()),
    path('detail/<int:id>', CategoryDetailUpdateDeleteAPIView.as_view()),
    path('check/', CategoryCheckAPIView.as_view()),
]
