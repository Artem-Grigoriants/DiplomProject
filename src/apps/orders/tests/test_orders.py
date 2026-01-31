from rest_framework.test import APITestCase
from rest_framework import status
from apps.orders.models import Order, OrderItem
from apps.users.models import User
from apps.products.models import Product
from .models import Order, OrderItem

class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword123")
        self.product = Product.objects.create(name="Test Product", price=100.00, stock=10)
        self.client.force_authenticate(user=self.user)

    def test_create_order(self):
        data = {
            "items": [
                {"product": self.product.id, "quantity": 2, "price": 100.00}
            ]
        }
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.first().product, self.product)

    def test_order_list(self):
        Order.objects.create(user=self.user)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)