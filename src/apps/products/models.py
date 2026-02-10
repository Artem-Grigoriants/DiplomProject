#Код определяет модели базы данных для приложения `products`.
#Эти модели представляют структуру данных, связанных с продуктами и их поставщиками в базе данных.

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    image = ThumbnailerImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    characteristics = models.JSONField(default=dict)  # To store key-value pairs for product characteristics
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    model = models.CharField(max_length=100, verbose_name='Модель')
    external_id = models.PositiveIntegerField(verbose_name='Внешний ID')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='infos', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = 'Информация о продуктах'

    def __str__(self):
        return f"Информация о {self.product.name} (Модель: {self.model})"

#Модели в файле:
# 1. **`Поставщик`**:
## - Представляет поставщика продукции.
## - Поля:
## - `name`: Название поставщика.
## - `contact_info`: Дополнительная контактная информация поставщика.
##
# 2. **`Категория`**:
## - Представляет категорию, к которой принадлежит продукт.
## - Поля:
## - `name`: Название категории.
## - `description`: Описание категории.
##
# 3. **`Продукт`**:
## - Представляет продукт в системе.
## - Поля:
## - `name`: Название продукта.
## - `category`: Внешний ключ, связывающий продукт с категорией.
## - `image`: Изображение продукта.
## - `description`: Подробное описание продукта.
## - `supplier`: Внешний ключ, связывающий продукт с поставщиком.
## - `characteristics`: Поле JSON для хранения пар ключ-значение для атрибутов продукта.
## - `price`: Цена продукта.
## - `stock`: Количество продукта на складе.
## - `created_at`: Метка времени создания продукта.
## - `updated_at`: Метка времени последнего обновления продукта.
##
# 4. **`Информация о продукте`**:
## - Дополнительная информация о продукте.
## - Поля:
## - `model`: Модель продукта.
## - `external_id`: Внешний идентификатор продукта.
## - `product`: Внешний ключ, связывающий информацию с продуктом.
