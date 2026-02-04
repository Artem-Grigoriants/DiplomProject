#Код определяет сериализаторы для приложения продуктов.
#Эти сериализаторы используются для преобразования сложных типов данных,
#таких как модели Django, в формат JSON и наоборот

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'supplier', 'characteristics', 'price', 'stock']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value