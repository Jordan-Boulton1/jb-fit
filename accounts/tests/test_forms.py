from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from allauth.account.models import EmailAddress
from accounts.forms import CustomSignupForm, CustomLoginForm
from accounts.models import UserProfile

class TestCustomSignupForm(TestCase):

    def test_valid_signup_form(self):
        form_data = {
            'email': 'testuser@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'gender': 'M'
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save(self.client)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'testuser@example.com')

        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.gender, 'Male')

    def test_invalid_signup_form(self):
        form_data = {
            'email': 'invalidemail',
            'first_name': '',
            'last_name': '',
            'password1': 'password',
            'password2': 'password123',
            'gender': 'M'
        }
        form = CustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

class TestCustomLoginForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='strongpassword123')
        EmailAddress.objects.create(user=self.user, email=self.user.email, verified=True, primary=True)

    def test_valid_login_form(self):
        form_data = {
            'login': 'testuser@example.com',
            'password': 'strongpassword123',
        }
        form = CustomLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_login_form(self):
        form_data = {
            'login': 'testuser@example.com',
            'password': 'wrongpassword',
        }
        form = CustomLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertIn('The email address and/or password you specified are not correct.', form.errors['__all__'])
