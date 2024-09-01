from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.


class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=40, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='media/images/go9xwcxemxj7sajmn1zf',
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )
    date_of_birth = models.DateField(blank=True, null=True)
    current_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    goal_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )


class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.weight} kg on "
            f"{self.entry_date.strftime('%Y-%m-%d')}"
        )

    def save(self, *args, **kwargs):
        # Round the weight to 2 decimal places before saving
        self.weight = Decimal(self.weight).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
        super().save(*args, **kwargs)


class ProgressPicture(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name="progress_pictures",
        on_delete=models.CASCADE
    )
    progress_image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.uploaded_at}"
