from django.test import TestCase
from apps.users.models import CustomUser

class CustomUserTests(TestCase):
    def test_create_user(self):
        """Tests if a user can be created."""
        user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword123",
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Tests if a superuser can be created."""
        admin_user = CustomUser.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword123",
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_str_representation(self):
        """Tests the string representation of the model."""
        user = CustomUser.objects.create(username="strtest")
        self.assertEqual(str(user), "strtest")