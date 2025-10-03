from rest_framework.test import APITestCase
from rest_framework import status
from apps.products.models import Product
from apps.users.models import CustomUser


class ProductViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", password="password123"
        )
        self.product = Product.objects.create(
            name="Initial Product", price=10.00, created_by=self.user
        )
        self.list_url = "/api/products/"

    def test_create_product_authenticated(self):
        """Authenticated users can create a product."""
        self.client.login(username="testuser", password="password123")
        data = {"name": "New Product", "price": 20.00}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_unauthenticated(self):
        """Unauthenticated users cannot create a new product."""
        data = {"name": "New Product", "price": 20.00}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(), 1)
