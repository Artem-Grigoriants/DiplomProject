from rest_framework.test import APITestCase
from rest_framework import status
from apps.products.models import Product, Supplier, Category
from apps.products.serializers import ProductSerializer

class ProductTests(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="test@example.com")
        self.category = Category.objects.create(name="Test Category", description="Test Description")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            supplier=self.supplier,
            category=self.category,
            characteristics={"color": "red", "size": "M"},
            price=100.00,
            stock=10
        )

    def test_product_serializer_validation(self):
        # Test valid data
        data = {
            "name": "New Product",
            "description": "New Description",
            "supplier": self.supplier.id,
            "characteristics": {"color": "blue", "size": "L"},
            "price": 50.00,
            "stock": 5
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # Test invalid price
        data["price"] = -10
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("price", serializer.errors)

        # Test invalid stock
        data["price"] = 50.00
        data["stock"] = -5
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("stock", serializer.errors)

    def test_product_list_view(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.product.name)