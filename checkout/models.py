# Import necessary modules and classes for defining models
from django.db import models  # Django's database models module
from django.contrib.auth.models import User
from plans.models import TrainingPlan
from decimal import Decimal, ROUND_HALF_UP


# Define the Order model
class Order(models.Model):
    # Link the order to a user; when the user is deleted,
    # their orders are also deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Link the order to a training plan;
    # when the plan is deleted, associated orders are also deleted
    training_plan = models.ForeignKey(
        TrainingPlan,
        on_delete=models.CASCADE
    )

    # Fields for storing customer's first and last names
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    # Field for storing customer's email address
    email = models.EmailField(null=False, blank=False)

    # Field for storing customer's phone number, optional
    phone_number = models.CharField(max_length=15, blank=True)

    # Field for storing the amount to be paid,
    # with a maximum of 5 digits and 2 decimal places
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    # Boolean field to track if the order has been paid, default is False
    paid = models.BooleanField(default=False)

    # Field for storing the timestamp when the order
    # was created, automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)

    # Field for storing the Stripe payment intent ID
    # for tracking payments, cannot be null or blank
    stripe_payment_intent_id = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    # String representation of the order, combining first name,
    # last name, and training plan name
    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - "
            f"{self.training_plan.name}"
        )

    # Override the save method to ensure the amount
    # is rounded to two decimal places
    def save(self, *args, **kwargs):
        # Round the amount to two decimal places using
        # ROUND_HALF_UP to avoid rounding issues
        self.amount = Decimal(self.amount).quantize(
            Decimal('0.01'),
            rounding=ROUND_HALF_UP
        )
        # Call the parent class's save method to save the instance
        super().save(*args, **kwargs)
