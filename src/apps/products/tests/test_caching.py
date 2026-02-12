import time
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.products.models import Product, Category, Supplier

class CachingTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name='Test Supplier')
        self.category = Category.objects.create(name='Test Category')
        for i in range(20):
            Product.objects.create(
                name=f'Product {i}',
                category=self.category,
                supplier=self.supplier,
                price=100 + i,
                stock=10
            )

    def test_product_list_caching(self):
        url = reverse('product-list')

        # Первый запрос (не из кэша)
        start_time = time.time()
        response1 = self.client.get(url)
        duration1 = time.time() - start_time
        self.assertEqual(response1.status_code, 200)

        # Второй запрос (должен быть из кэша)
        start_time = time.time()
        response2 = self.client.get(url)
        duration2 = time.time() - start_time
        self.assertEqual(response2.status_code, 200)

        # Проверяем, что второй запрос был быстрее
        self.assertLess(duration2, duration1)
        print(f"Первый запрос: {duration1:.4f}s, Второй (cached) запрос: {duration2:.4f}s")


