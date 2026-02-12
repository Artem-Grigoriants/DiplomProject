#Код определяет представления для приложения `products`.
#Эти представления обрабатывают HTTP-запросы и возвращают соответствующие ответы,
#такие как списки товаров или подробную информацию о конкретном товаре.
#Представления реализованы с использованием классовых представлений Django REST Framework.

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer
from cacheops import cached_as

class ProductListView(ListAPIView):
    @cached_as(Product)
    def get_queryset(self):
        return Product.objects.select_related('supplier').all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['supplier', 'price']
    search_fields = ['name', 'description', 'characteristics']