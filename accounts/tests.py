from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class CustomUserTests(TestCase):
    def test_cteate_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Yevhenii", email="yevhenii@admin.com", password="testpass123"
        )
        self.assertEqual(user.username, "Yevhenii")
        self.assertEqual(user.email, "yevhenii@admin.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_supersuer(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="super@admin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "super@admin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
