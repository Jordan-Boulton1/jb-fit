# Import necessary modules and classes for testing
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse  # For resolving URLs in tests
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from allauth.account.models import EmailAddress
from unittest.mock import patch
from accounts.models import UserProfile  # Import UserProfile model
from plans.models import TrainingPlan
from checkout.models import Order
from decimal import Decimal


# Define test cases for checkout views
class CheckoutViewsTestCase(TestCase):

    def setUp(self):
        # Set up a test client for making requests
        self.client = Client()
        # Create a user and set up their profile
        self.user = User.objects.create_user(
            email='testuser@test.com',
            username="test",
            password='testpass',
            first_name='testy',
            last_name='testy'
        )

        # Create a user profile linked to the created user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            phone_number='1234567890'
        )

        # Create a sample training plan for testing
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

        # Log in the user using the client and Allauth's login view
        self.client.post(reverse('account_login'), {
            'login': 'testuser@test.com',
            'password': 'testpass'
        })

    # Test the checkout view with a valid form submission
    @patch('stripe.PaymentIntent.create')
    @patch('stripe.PaymentIntent.modify')
    def test_checkout_view_post_valid(self, mock_modify, mock_create):
        """Test the checkout view with a valid form submission."""
        # Mock the Stripe PaymentIntent create and modify responses
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }

        # Simulate a POST request to the checkout view with valid form data
        response = self.client.post(
            reverse('checkout', args=[self.training_plan.id]), {
                'first_name': 'testy',
                'last_name': 'testy',
                'email': 'testuser@test.com',
                'phone_number': '1234567890',
                'client_secret': 'test_pid_secret'
            }, follow=True
        )

        # Check that the response redirects to the checkout success page
        self.assertRedirects(response, reverse('checkout_success', args=[1]))
        # Retrieve the created order from the database
        order = Order.objects.get(id=1)
        # Verify that the order fields match the expected values
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.training_plan, self.training_plan)
        self.assertEqual(order.amount, Decimal('50.00'))
        self.assertEqual(order.stripe_payment_intent_id, 'test_pid')

    # Test the checkout view with an invalid form submission
    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_post_invalid_form(self, mock_create):
        """Test the checkout view with an invalid form submission."""
        # Mock the Stripe PaymentIntent create response
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }

        # Simulate a POST request to the checkout view
        # with invalid form data (missing first_name)
        response = self.client.post(
            reverse('checkout', args=[self.training_plan.id]), {
                'first_name': '',
                'last_name': 'testy',
                'email': 'testuser@test.com',
                'phone_number': '1234567890',
                'client_secret': 'test_pid_secret'
            }, follow=True
        )

        # Check that the response redirects back to
        # the checkout page due to form errors
        self.assertRedirects(
            response,
            reverse('checkout', args=[self.training_plan.id])
        )

    # Test the checkout view on a GET request
    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_get(self, mock_create):
        """Test the checkout view on a GET request."""
        # Mock the Stripe PaymentIntent create response
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }

        # Temporarily change the STRIPE_PUBLIC_KEY
        # setting and test if a warning is displayed
        with self.settings(STRIPE_PUBLIC_KEY=''):
            response = self.client.get(
                reverse('checkout', args=[self.training_plan.id])
            )
            # Retrieve messages from the response and check if
            # the warning about missing Stripe public key is present
            messages = list(get_messages(response.wsgi_request))
            self.assertTrue(any(
                'Stripe public key is missing' in
                str(message) for message in messages)
            )

        # Simulate a GET request to the checkout view
        response = self.client.get(
            reverse('checkout', args=[self.training_plan.id])
        )
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        # Check that the response context
        # includes the order form and training plan
        self.assertIn('order_form', response.context)
        self.assertIn('training_plan', response.context)
        self.assertEqual(response.context['training_plan'], self.training_plan)
        # Verify that the Stripe public key is included in the context
        self.assertEqual(
            response.context['stripe_public_key'], settings.STRIPE_PUBLIC_KEY
        )

    # Test the checkout view with a missing Stripe public key
    @patch('stripe.PaymentIntent.create')
    def test_checkout_view_missing_stripe_public_key(self, mock_create):
        """Test the checkout view with missing Stripe public key."""
        # Mock the Stripe PaymentIntent create response
        mock_create.return_value = {
            'client_secret': 'test_client_secret',
            'id': 'test_pid'
        }
        # Temporarily change the STRIPE_PUBLIC_KEY setting
        # and test if a warning is displayed
        with self.settings(STRIPE_PUBLIC_KEY=''):
            response = self.client.get(
                reverse('checkout', args=[self.training_plan.id])
            )
            # Retrieve messages from the response and check if the
            # warning about missing Stripe public key is present
            messages = list(get_messages(response.wsgi_request))
            self.assertTrue(
                any('Stripe public key is missing'
                    in str(message) for message in messages)
            )

    # Test the checkout success view
    def test_checkout_success_view(self):
        """Test the checkout success view."""
        # Create an order instance for testing the success view
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
        # Simulate a GET request to the checkout
        # success view with the created order
        response = self.client.get(
            reverse('checkout_success', args=[order.id])
        )
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        # Check that the response context includes the order
        self.assertIn('order', response.context)
        self.assertEqual(response.context['order'], order)
