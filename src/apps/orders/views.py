from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import Contact, Order, OrderItem, Cart, CartItem
from apps.products.models import Product as ProductBase  # Corrected import
from .serializers import (
    UserRegistrationSerializer,
    ProductSerializer,
    CartSerializer,
    ContactSerializer,
    OrderSerializer,
    OrderItemSerializer,
)
from django.shortcuts import get_object_or_404

User = get_user_model()

class CartView(APIView):
    """
    API view for cart operations
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = get_object_or_404(ProductBase, id=product_id)  # Corrected to use ProductBase
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        cart_item = get_object_or_404(CartItem, id=pk, cart__user=request.user)
        cart_item.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    """
    API view for user login
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegistrationView(APIView):
    """
    API view for user registration
    """
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(APIView):
    """
    API view for listing products
    """
    def get(self, request):
        products = ProductBase.objects.all()  # Corrected to use ProductBase
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactView(APIView):
    """
    API view for managing user contacts
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contacts = Contact.objects.filter(user=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = get_object_or_404(Contact, id=pk, user=request.user)
        contact.delete()
        return Response({'message': 'Contact deleted'}, status=status.HTTP_204_NO_CONTENT)


class OrderConfirmationView(APIView):
    """
    API view for confirming orders
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user, status='new')
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                shop=item.product.shop,
                quantity=item.quantity
            )
        cart.items.all().delete()
        return Response({'message': 'Order confirmed'}, status=status.HTTP_201_CREATED)


class OrderListView(APIView):
    """
    API view for listing user orders
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Пояснение:
# LoginView: Обрабатывает вход пользователя путем аутентификации учетных данных.
# RegistrationView: Позволяет новым пользователям регистрироваться.
# ProductListView: Возвращает список всех доступных товаров.
# CartView: Обрабатывает операции с корзиной (просмотр, добавление, удаление товаров).
# ContactView: Управляет контактами пользователя (просмотр, добавление, удаление).
# OrderConfirmationView: Подтверждает заказ, создавая заказ из корзины.
# OrderListView: Отображает все заказы для аутентифицированного пользователя.