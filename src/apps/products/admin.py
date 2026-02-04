#Код регистрирует модель Product в административном интерфейсе Django.
from django.contrib import admin
from .models import Product

#Проверяем, зарегистрирована ли модель уже.
if not admin.site.is_registered(Product):
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('name', 'supplier', 'price', 'stock')
        search_fields = ('name', 'supplier__name')
        list_filter = ('supplier',)