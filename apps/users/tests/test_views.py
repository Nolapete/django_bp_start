from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import CustomUser


class CustomUserViewSetTests(APITestCase):
    def setUp(self):
        self.user_data = {"username": "testuser", "password": "password123"}
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.list_url = "/api/users/"

    def test_list_users_authenticated(self):
        """Authenticated users can retrieve the user list."""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_users_unauthenticated(self):
        """Unauthenticated users cannot retrieve the user list."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
