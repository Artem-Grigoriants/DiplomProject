#Код определяет модели базы данных для приложения `products`.
#Эти модели представляют структуру данных, связанных с продуктами и их поставщиками в базе данных.

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    characteristics = models.JSONField(default=dict)  # To store key-value pairs for product characteristics
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Модели в файле:
# 1. **`Поставщик`**:
## - Представляет поставщика продукции.
## - Поля:
## - `name`: Название поставщика.
## - `contact_info`: Дополнительная контактная информация поставщика.
##
# 2. **`Продукт`**:
## - Представляет продукт в системе.
## - Поля:
## - `name`: Название продукта.
## - `description`: Подробное описание продукта. — `supplier`: внешний ключ, связывающий продукт с поставщиком.
## — `characteristics`: поле JSON для хранения пар ключ-значение для атрибутов продукта.
## — `price`: цена продукта.
## — `stock`: количество продукта на складе.
## — `created_at`: метка времени создания продукта.
## — `updated_at`: метка времени последнего обновления продукта.
