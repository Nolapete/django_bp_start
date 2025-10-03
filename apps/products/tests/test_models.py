from django.test import TestCase
from apps.products.models import Product
from apps.users.models import CustomUser

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="creator")
        self.product = Product.objects.create(
            name="Test Product",
            price=19.99,
            created_by=self.user,
        )

    def test_product_creation(self):
        """Tests if a product is created correctly."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.created_by, self.user)

    def test_product_str_representation(self):
        """Tests the string representation of the product model."""
        self.assertEqual(str(self.product), "Test Product")