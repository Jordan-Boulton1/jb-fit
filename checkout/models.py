from django.db import models
from django.contrib.auth.models import User
from plans.models import TrainingPlan
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_plan = models.ForeignKey(
        TrainingPlan,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent_id = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - "
            f"{self.training_plan.name}"
        )
    
    def save(self, *args, **kwargs):
        # Ensure the amount is rounded to two decimal places
        self.amount = Decimal(self.amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        super().save(*args, **kwargs)
