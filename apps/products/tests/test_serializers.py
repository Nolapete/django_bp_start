from rest_framework.test import APITestCase
from apps.products.serializers import ProductSerializer
from apps.products.models import Product
from apps.users.models import CustomUser


class ProductSerializerTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password123")
        self.product = Product.objects.create(
            name="Test Product",
            price=19.99,
            created_by=self.user
        )

    def test_serializer_with_valid_data(self):
        """Tests the serializer with valid data."""
        data = {
            "name": "New Product",
            "price": 25.50
        }
        # A ModelSerializer will automatically handle the read_only `created_by` field.
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # Check that the validated data matches the input
        self.assertEqual(serializer.validated_data["name"], "New Product")
        self.assertEqual(serializer.validated_data["price"], 25.50)

    def test_serializer_with_invalid_data(self):
        """Tests the serializer with invalid data."""
        # Missing required 'name' field
        data = {
            "price": 10.00
        }
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_serializer_with_existing_instance(self):
        """Tests serializing an existing Product instance."""
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data

        self.assertEqual(data["name"], "Test Product")
        self.assertEqual(float(data["price"]), 19.99)
        self.assertEqual(data["created_by"], self.user.id)

    def test_serializer_create(self):
        """Tests if the serializer can create a new Product instance."""
        # Because 'created_by' is read_only, it should not be provided in the data.
        data = {
            "name": "Another Product",
            "price": 30.00
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # You must provide the 'created_by' field during save for testing purposes.
        product_instance = serializer.save(created_by=self.user)

        self.assertIsInstance(product_instance, Product)
        self.assertEqual(product_instance.name, "Another Product")
        self.assertEqual(product_instance.created_by, self.user)
