from rest_framework import generics, filters

from .models import Category
from .serializers import CategorySerializer


# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params is not None:
#             return True
#         return super().get_search_fields(view, request)


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
    search_fields = ['title']

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)
