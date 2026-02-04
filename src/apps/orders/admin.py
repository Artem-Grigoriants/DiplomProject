#Код для определения административного интерфейса приложения `orders`.
#Он настраивает отображение и управление моделями,
#такими как `Shop`, `Category`, `Order` и другими, в панели администратора Django.

from django.contrib import admin
from .models import (
    Shop, Category, ProductInfo, Parameter, ProductParameter,
    Order, OrderItem, Contact, Cart, CartItem
)
from apps.products.models import Product as ProductBase  # Corrected import


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', 'parent__name')


@admin.register(ProductBase)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'price', 'stock')
    search_fields = ('name', 'supplier__name')
    list_filter = ('supplier',)


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'shop', 'quantity', 'price', 'price_rrc')
    search_fields = ('product__name', 'shop__name')
    list_filter = ('shop',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('product_info', 'parameter', 'value')
    search_fields = ('product_info__product__name', 'parameter__name', 'value')
    list_filter = ('parameter',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dt', 'status')
    search_fields = ('user__email', 'status')
    list_filter = ('status', 'dt')
    date_hierarchy = 'dt'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'shop', 'quantity')
    search_fields = ('order__id', 'product__name', 'shop__name')
    list_filter = ('shop',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'value')
    search_fields = ('user__email', 'value')
    list_filter = ('type',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)
    date_hierarchy = 'created_at'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__email', 'product__name')
    list_filter = ('cart',)

# Пояснение:
# list_display: Задает поля для отображения в списке административной панели для каждой модели.
# search_fields: Добавляет строку поиска в административный интерфейс для быстрой фильтрации.
# list_filter: Добавляет фильтры в боковую панель для упрощения навигации.
# date_hierarchy: Добавляет навигацию по полям с датами с возможностью детализации.
