from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
# from .forms import CustomUserCreationForm
# from .views import SignupPageView


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


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'I should not be here')


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'I should not be here')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)


class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@mail.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'I should not be here')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)







