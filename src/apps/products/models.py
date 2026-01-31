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