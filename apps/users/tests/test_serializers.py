from rest_framework.test import APITestCase
from apps.users.serializers import CustomUserSerializer
from apps.users.models import CustomUser
from tenants.models import Tenant  # Assuming 'tenants' is the app name


class CustomUserSerializerTests(APITestCase):
    def setUp(self):
        # Create a tenant for the tests to use
        self.tenant = Tenant.objects.create(
            schema_name="testschema", name="Test Tenant"
        )

    def test_serializer_with_valid_data(self):
        """Tests the serializer with valid data."""
        data = {
            "username": "validuser",
            "email": "valid@example.com",
            "tenant": self.tenant.id,  # Provide the tenant ID here
        }
        serializer = CustomUserSerializer(data=data)

        # Adding a temporary print statement to see the errors
        # This is for debugging purposes and can be removed once the test passes.
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)

        self.assertTrue(
            serializer.is_valid(),
            "Serializer should be valid with all required fields.",
        )
        self.assertEqual(serializer.validated_data["username"], "validuser")

    def test_serializer_with_invalid_data(self):
        """Tests the serializer with invalid data."""
        # Ensure invalid data is still handled correctly.
        data = {"username": "", "email": "invalid"}
        serializer = CustomUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)
        self.assertIn("email", serializer.errors)
        self.assertIn("tenant", serializer.errors)
