from django.test import TestCase
from plans.models import TrainingPlan


class TrainingPlanModelTest(TestCase):
    """
    Test case for the TrainingPlan model to ensure its functionality.
    """

    def setUp(self):
        """
        Sets up a sample TrainingPlan instance for testing.
        """
        # Create a sample TrainingPlan instance
        self.training_plan = TrainingPlan.objects.create(
            name="Sample Plan",
            description="This is a sample training plan description.",
            price=99.99
        )

    def test_training_plan_creation(self):
        """
        Tests if the TrainingPlan instance is created with correct values.
        """
        # Check that the name, description, and price are correctly set
        self.assertEqual(self.training_plan.name, "Sample Plan")
        self.assertEqual(
            self.training_plan.description,
            "This is a sample training plan description."
        )
        self.assertEqual(self.training_plan.price, 99.99)

    def test_training_plan_string_representation(self):
        """
        Tests the string representation of the TrainingPlan model.
        """
        # Verify that the string representation matches the plan's name
        self.assertEqual(str(self.training_plan), "Sample Plan")

    def test_name_max_length(self):
        """
        Tests the max_length constraint on the name field.
        """
        # Retrieve the max_length attribute from the name field
        max_length = self.training_plan._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_price_max_digits_and_decimal_places(self):
        """
        Tests the max_digits and decimal_places constraints on the price field.
        """
        # Retrieve max_digits and decimal_places attributes from the price field  # noqa
        max_digits = self.training_plan._meta.get_field('price').max_digits
        decimal_places = self.training_plan._meta.get_field('price').decimal_places  # noqa
        self.assertEqual(decimal_places, 2)

    def test_created_at_auto_now_add(self):
        """
        Tests if the created_at field is automatically set on creation.
        """
        # Check that the created_at field is not None
        self.assertIsNotNone(self.training_plan.created_at)
