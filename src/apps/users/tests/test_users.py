from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
            "company": "Test Company",
            "position": "Developer",
            "type": "buyer"
        }
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.company, "Test Company")
        self.assertEqual(user.position, "Developer")
        self.assertEqual(user.type, "buyer")

    def test_user_login(self):
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
            company="Test Company",
            position="Developer",
            type="buyer"
        )
        data = {"email": "testuser@example.com", "password": "testpassword123"}
        response = self.client.post('/auth/jwt/create/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)