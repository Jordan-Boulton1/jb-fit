# Import necessary modules and classes for testing
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from plans.models import TrainingPlan
from checkout.models import Order  # Import the Order model to be tested
from decimal import Decimal  # For precise decimal operations

# Get the user model (usually Django's default User model)
User = get_user_model()


# Define test cases for the Order model
class OrderModelTest(TestCase):

    def setUp(self):
        # Create a sample user and training plan for testing
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.training_plan = TrainingPlan.objects.create(
            name='Test Plan',
            description='A sample training plan',
            price=50.00
        )

    # Test that an Order instance can be created successfully
    def test_order_creation(self):
        """Test that an Order instance can be created successfully."""
        order = Order.objects.create(
            user=self.user,  # Associate the order with the test user
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='1234567890',
            amount=Decimal('49.99'),  # Set the amount for the order
            paid=True,  # Mark the order as paid
            stripe_payment_intent_id='pi_123456789'
        )
        # Check that the order is an instance of the Order model
        self.assertIsInstance(order, Order)
        # Verify that each field on the order matches the expected values
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.training_plan, self.training_plan)
        self.assertEqual(order.first_name, 'John')
        self.assertEqual(order.last_name, 'Doe')
        self.assertEqual(order.email, 'johndoe@example.com')
        self.assertEqual(order.phone_number, '1234567890')
        self.assertEqual(order.amount, Decimal('49.99'))
        self.assertTrue(order.paid)
        self.assertEqual(order.stripe_payment_intent_id, 'pi_123456789')
        self.assertIsNotNone(order.created_at)

    # Test that Order enforces required fields by using full_clean()
    def test_order_required_fields(self):
        """Test that Order enforces required fields by using full_clean()."""
        # Test case: Missing first_name field
        order = Order(
            user=self.user,
            training_plan=self.training_plan,
            last_name='Doe',
            email='johndoe@example.com',
            amount=Decimal('49.99'),
            stripe_payment_intent_id='pi_123456789'
        )
        # Check that a ValidationError is raised
        # when required fields are missing
        with self.assertRaises(ValidationError):
            order.full_clean()

        # Test case: Missing last_name field
        order = Order(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            email='johndoe@example.com',
            amount=Decimal('49.99'),
            stripe_payment_intent_id='pi_123456789'
        )
        with self.assertRaises(ValidationError):
            order.full_clean()

        # Test case: Missing email field
        order = Order(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            amount=Decimal('49.99'),
            stripe_payment_intent_id='pi_123456789'
        )
        with self.assertRaises(ValidationError):
            order.full_clean()

        # Test case: Missing training_plan field
        order = Order(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            amount=Decimal('49.99'),
            stripe_payment_intent_id='pi_123456789'
        )
        with self.assertRaises(ValidationError):
            order.full_clean()

    # Test the string representation of an Order instance
    def test_str_representation(self):
        """Test the string representation of an Order instance."""
        order = Order.objects.create(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='1234567890',
            amount=Decimal('49.99'),
            paid=False,
            stripe_payment_intent_id='pi_123456789'
        )
        # Expected string representation combining first name,
        # last name, and training plan name
        expected_str = f"John Doe - {self.training_plan.name}"
        self.assertEqual(str(order), expected_str)

    # Test that the paid field defaults to False when not specified
    def test_paid_field_default(self):
        """Test that the paid field defaults to False."""
        order = Order.objects.create(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='1234567890',
            amount=Decimal('49.99'),
            stripe_payment_intent_id='pi_123456789'
        )
        # Check that the paid field defaults to False
        self.assertFalse(order.paid)

    # Test that the amount field maintains the correct decimal precision
    def test_amount_decimal_precision(self):
        """
        Test that the amount field maintains the
        correct decimal precision.
        """
        order = Order.objects.create(
            user=self.user,
            training_plan=self.training_plan,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='1234567890',
            amount=Decimal('49.995')
        )
        # Check that the amount is rounded to two decimal places as expected
        self.assertEqual(order.amount, Decimal('50.00'))
