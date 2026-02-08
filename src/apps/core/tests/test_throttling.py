from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class ThrottlingTests(APITestCase):
    """
    Тесты для проверки механизма троттлинга.
    """

    def test_anon_rate_throttle(self):
        """
        Проверяет, что для анонимного пользователя срабатывает ограничение
        после 100 запросов.
        """
        url = reverse('product-list')  # Используем эндпоинт списка продуктов

        # Выполняем 100 запросов, которые должны быть успешными
        for i in range(100):
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK, f"Request {i+1} failed")

        # 101-й запрос должен быть заблокирован
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

