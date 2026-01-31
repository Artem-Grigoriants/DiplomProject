from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import path, include
from django.contrib.auth import get_user_model

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

User = get_user_model()

class UserTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Test Street",
            "phone_number": "1234567890"
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_user_login(self):
        user = User.objects.create_user(username="testuser", password="testpassword123")
        data = {"username": "testuser", "password": "testpassword123"}
        response = self.client.post('/auth/jwt/create/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)