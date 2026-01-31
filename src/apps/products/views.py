# src/apps/products/views.py
# from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from .models import Product
# from .serializers import ProductSerializer
#
# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['supplier', 'price']
#     search_fields = ['name', 'description', 'characteristics']

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Product
from .serializers import ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.select_related('supplier').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['supplier', 'price']
    search_fields = ['name', 'description', 'characteristics']