#Registers the Product model in the Django admin interface.
from django.contrib import admin
from .models import Product

# Check if the model is already registered
if not admin.site.is_registered(Product):
    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('name', 'supplier', 'price', 'stock')
        search_fields = ('name', 'supplier__name')
        list_filter = ('supplier',)