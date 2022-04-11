from rest_framework import generics, filters

from .models import Category
from .serializers import CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    """
    List of categories
    """

    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)


class CategoryCreateAPIView(generics.CreateAPIView):
    """
    Creating category
    """

    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update, detail category
    """

    model = Category
    serializer_class = CategorySerializer


class CategoryCheckAPIView(generics.ListAPIView):
    """
    Cheking is category exist
    """

    model = Category
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)
