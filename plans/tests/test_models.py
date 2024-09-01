from django.test import TestCase
from plans.models import TrainingPlan

class TrainingPlanModelTest(TestCase):

    def setUp(self):
        # Set up a sample TrainingPlan instance
        self.training_plan = TrainingPlan.objects.create(
            name="Sample Plan",
            description="This is a sample training plan description.",
            price=99.99
        )

    def test_training_plan_creation(self):
        # Test if the training plan is created successfully
        self.assertEqual(self.training_plan.name, "Sample Plan")
        self.assertEqual(self.training_plan.description, "This is a sample training plan description.")
        self.assertEqual(self.training_plan.price, 99.99)

    def test_training_plan_string_representation(self):
        # Test the string representation of the TrainingPlan model
        self.assertEqual(str(self.training_plan), "Sample Plan")

    def test_name_max_length(self):
        # Test the max_length constraint on the name field
        max_length = self.training_plan._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_price_max_digits_and_decimal_places(self):
        # Test the max_digits and decimal_places constraints on the price field
        max_digits = self.training_plan._meta.get_field('price').max_digits
        decimal_places = self.training_plan._meta.get_field('price').decimal_places
        self.assertEqual(max_digits, 5)
        self.assertEqual(decimal_places, 2)

    def test_created_at_auto_now_add(self):
        # Test if created_at is set automatically on creation
        self.assertIsNotNone(self.training_plan.created_at)
