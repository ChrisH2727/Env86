from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='Env86', email='chris@hullbrook.net', password='Redant3009'
                                        )
        self.assertEqual(user.username, 'Env86')
        self.assertEqual(user.email, 'chris@hullbrook.net')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='superadmin', email='superadmin@mail.com',
                                                   password='Redant3009'
                                                   )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
