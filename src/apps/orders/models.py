#Код `models.py` определяет модели базы данных для приложения `orders`

from django.db import models
from django.conf import settings
from apps.products.models import Product as ProductBase

STATE_CHOICES = (
    ('basket', 'Basket'),
    ('new', 'New'),
    ('confirmed', 'Confirmed'),
    ('assembled', 'Assembled'),
    ('sent', 'Sent'),
    ('delivered', 'Delivered'),
    ('canceled', 'Canceled'),
)

CONTACT_TYPE_CHOICES = (
    ('phone', 'Phone'),
    ('email', 'Email'),
    ('address', 'Address'),
)


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,  # Added on_delete argument
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name='Parent Category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE, related_name='product_infos', verbose_name='Product')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='product_infos', verbose_name='Shop')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    price_rrc = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Recommended Retail Price')

    class Meta:
        verbose_name = 'Product Info'
        verbose_name_plural = 'Product Infos'
        unique_together = ('product', 'shop')

    def __str__(self):
        return f"{self.product.name} - {self.shop.name}"


class Parameter(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')

    class Meta:
        verbose_name = 'Parameter'
        verbose_name_plural = 'Parameters'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, related_name='product_parameters', verbose_name='Product Info')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, related_name='product_parameters', verbose_name='Parameter')
    value = models.CharField(max_length=100, verbose_name='Value')

    class Meta:
        verbose_name = 'Product Parameter'
        verbose_name_plural = 'Product Parameters'
        unique_together = ('product_info', 'parameter')

    def __str__(self):
        return f"{self.parameter.name}: {self.value}"


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"Cart of {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Cart')
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Product')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name='User')
    dt = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    status = models.CharField(max_length=15, choices=STATE_CHOICES, verbose_name='Status')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-dt']

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name='Order')
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE, related_name='order_items', verbose_name='Product')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='order_items', verbose_name='Shop')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Contact(models.Model):
    type = models.CharField(max_length=10, choices=CONTACT_TYPE_CHOICES, verbose_name='Type')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts', verbose_name='User')
    value = models.CharField(max_length=255, verbose_name='Value')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.type}: {self.value}"

# 1. **Shop**: Представляет магазин с полем `name`.
# 2. **Category**: Представляет категории товаров с поддержкой иерархических связей с помощью поля `parent`.
# 3. **ProductInfo**: Связывает товары с магазинами, включая такие детали, как `quantity`, `price` и `price_rrc`.
# 4. **Parameter**: Представляет параметры товара (например, цвет, размер).
# 5. **ProductParameter**: Связывает `ProductInfo` с `Parameter` с полем `value`.
# 6. **Cart**: Представляет корзину покупок, связанную с пользователем.
# 7. **CartItem**: Представляет товары в корзине, связывая `товар` с `корзиной` и `количеством`.
# 8. **Order**: Представляет заказ, сделанный пользователем, с полями для `статуса` и `даты`.
# 9. **OrderItem**: Представляет товары в заказе, связывая `товар` и `магазин` с `заказом`.
# 10. **Contact**: Хранит контактную информацию пользователя, такую ​​как `телефон`, `электронная почта` или `адрес`.
# Каждая модель включает метаданные (например, `verbose_name`, `ordering`) и строковые представления для лучшей читаемости в административном интерфейсе.