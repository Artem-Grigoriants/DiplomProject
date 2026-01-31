from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Contact, Order, OrderItem, Cart, CartItem
from apps.products.models import Product

# Get the User model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'supplier')

class CartSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'created_at')

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'type', 'value', 'user')

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'dt', 'status', 'items')

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'shop', 'quantity')