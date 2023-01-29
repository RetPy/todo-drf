from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.todos.views import *


router = DefaultRouter()
router.register(
    'todo',
    TodoViewSet,
    basename='todo',
)
router.register(
    'category',
    CategoryViewSet,
    basename='category'
)

urlpatterns = router.urls
