from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from allauth.account.models import EmailAddress
from unittest.mock import patch
from accounts.models import UserProfile
from plans.models import TrainingPlan
from checkout.models import Order
from decimal import Decimal


class CheckoutViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Create a user and set up their profile
        self.user = User.objects.create_user(
            email='testuser@test.com',
            username="test",
            password='testpass',
            first_name='testy',
            last_name='testy'
        )

        self.user_profile = UserProfile.objects.create(
            user=self.user,
            phone_number='1234567890'
        )
        self.training_plan = TrainingPlan.objects.create(
            name='Test Plan',
            description='A sample training plan',
            price=50.00
        )

        # Mark the email as verified to simulate a real user login with Allauth
        EmailAddress.objects.create(
            user=self.user,
            email='testuser@test.com',
            verified=True,
            primary=True
        )

        # Use the client to log in through Allauth's login view
        self.client.post(reverse('account_login'), {
            'login': 'testuser@test.com',
            'password': 'testpass'
        })

    @patch('stripe.PaymentIntent.create')
    @patch('stripe.PaymentIntent.modify')
    def test_checkout_view_post_valid(self, mock_modify, mock_create):
        """Test the checkout view with a valid form submission."""
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }
        response = self.client.post(
            reverse('checkout', args=[self.training_plan.id]), {
                'first_name': 'testy',
                'last_name': 'testy',
                'email': 'testuser@test.com',
                'phone_number': '1234567890',
                'client_secret': 'test_pid_secret'
            }, follow=True
        )

        self.assertRedirects(response, reverse('checkout_success', args=[1]))
        order = Order.objects.get(id=1)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.training_plan, self.training_plan)
        self.assertEqual(order.amount, Decimal('50.00'))
        self.assertEqual(order.stripe_payment_intent_id, 'test_pid')

    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_post_invalid_form(self, mock_create):
        """Test the checkout view with an invalid form submission."""
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }

        response = self.client.post(
            reverse('checkout', args=[self.training_plan.id]), {
                'first_name': '',
                'last_name': 'testy',
                'email': 'testuser@test.com',
                'phone_number': '1234567890',
                'client_secret': 'test_pid_secret'
            }, follow=True
        )

        self.assertRedirects(
            response,
            reverse('checkout', args=[self.training_plan.id])
        )

    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_get(self, mock_create):
        """Test the checkout view on a GET request."""
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }

        # Temporarily change the STRIPE_PUBLIC_KEY setting
        with self.settings(STRIPE_PUBLIC_KEY=''):
            response = self.client.get(
                reverse('checkout', args=[self.training_plan.id])
            )
            messages = list(get_messages(response.wsgi_request))
            self.assertTrue(any(
                'Stripe public key is missing' in str(message) for message in messages)  # noqa
            )

        response = self.client.get(
            reverse('checkout', args=[self.training_plan.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('order_form', response.context)
        self.assertIn('training_plan', response.context)
        self.assertEqual(response.context['training_plan'], self.training_plan)
        self.assertEqual(
            response.context['stripe_public_key'], settings.STRIPE_PUBLIC_KEY
        )

    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_missing_stripe_public_key(self, mock_create):
        """Test the checkout view with missing Stripe public key."""
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }
        # Temporarily change the STRIPE_PUBLIC_KEY setting
        with self.settings(STRIPE_PUBLIC_KEY=''):
            response = self.client.get(
                reverse('checkout', args=[self.training_plan.id])
            )
            messages = list(get_messages(response.wsgi_request))
            self.assertTrue(
                any('Stripe public key is missing' in str(message) for message in messages)  # noqa
            )

    def test_checkout_success_view(self):
        """Test the checkout success view."""
        order = Order.objects.create(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='1234567890',
            amount=Decimal('50.00'),
            stripe_payment_intent_id='test_pid'
        )
        response = self.client.get(
            reverse('checkout_success', args=[order.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertIn('order', response.context)
        self.assertEqual(response.context['order'], order)
