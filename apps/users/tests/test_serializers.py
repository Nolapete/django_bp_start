from rest_framework.test import APITestCase
from apps.users.serializers import CustomUserSerializer
from apps.users.models import CustomUser


class CustomUserSerializerTests(APITestCase):
    def test_serializer_with_valid_data(self):
        """Tests the serializer with valid data."""
        data = {"username": "validuser", "email": "valid@example.com"}
        serializer = CustomUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["username"], "validuser")

    def test_serializer_with_invalid_data(self):
        """Tests the serializer with invalid data."""
        data = {"username": "", "email": "invalid"}
        serializer = CustomUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors), 2)
