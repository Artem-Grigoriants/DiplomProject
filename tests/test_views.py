from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "password123",
            "first_name": "Test",
            "last_name": "User",
            "is_supplier": True,
            "is_client": False
        }
        self.user = User.objects.create_user(
            email="existinguser@example.com",
            username="existinguser",
            password="password123",
            is_supplier=False,
            is_client=True
        )

    def test_user_registration_valid(self):
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.user_data['email'])

    def test_user_registration_invalid_email(self):
        self.user_data['email'] = "invalid-email"
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_user_registration_duplicate_email(self):
        self.user_data['email'] = "existinguser@example.com"
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_user_registration_missing_roles(self):
        self.user_data['is_supplier'] = False
        self.user_data['is_client'] = False
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_user_detail_view(self):
        self.client.login(email="existinguser@example.com", password="password123")
        response = self.client.get('/api/auth/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], "existinguser@example.com")