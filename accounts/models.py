from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.


class UserProfile(models.Model):
    """
    User profile model that extends the
    built-in User model with additional fields.
    """
    # One-to-one relationship with the built-in User model.
    # When the user is deleted, the associated profile is also deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Optional phone number field with a maximum length of 15 characters.
    phone_number = models.CharField(max_length=15, blank=True)

    # Optional address field with a maximum length of 40 characters.
    address = models.TextField(max_length=40, blank=True)

    # Image field to store profile pictures.
    # Images are uploaded to the 'images/' directory.
    # A default image is set if none is uploaded.
    image = models.ImageField(
        upload_to='images/',
        default='media/images/go9xwcxemxj7sajmn1zf',
        null=True,
        blank=True
    )

    # Gender field with choices restricted to 'Male', 'Female', or 'Other'.
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )

    # Optional date of birth field.
    date_of_birth = models.DateField(blank=True, null=True)

    # Optional field for storing the user's current weight.
    # The weight is stored as a decimal
    # with up to 5 digits and 2 decimal places.
    current_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Optional field for storing the user's height.
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Optional field for storing the user's goal weight.
    goal_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )


class WeightLog(models.Model):
    """
    Model to log the user's weight entries over time.
    """
    # Foreign key relationship with the User model.
    # When the user is deleted, the related weight logs are also deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Field to store the weight entry.
    # Weight is stored as a decimal with up to 5 digits and 2 decimal places.
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    # Field to store the date and time
    # when the weight entry was created.
    # Automatically set to the current
    # date and time when the record is created.
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the weight log entry, including
        # the username, weight, and entry date.
        return (
            f"{self.user.username} - {self.weight} kg on "
            f"{self.entry_date.strftime('%Y-%m-%d')}"
        )

    def save(self, *args, **kwargs):
        # Round the weight to 2 decimal places before saving to the database.
        self.weight = Decimal(self.weight).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
        # Call the parent class's save method to save the record.
        super().save(*args, **kwargs)


class ProgressPicture(models.Model):
    """
    Model to store progress pictures uploaded by the user.
    """
    # Foreign key relationship with the UserProfile model.
    # Related progress pictures are deleted
    # when the associated user profile is deleted.
    user = models.ForeignKey(
        UserProfile,
        related_name="progress_pictures",
        on_delete=models.CASCADE
    )

    # Field to store the progress image.
    # Images are uploaded to the 'images/' directory.
    progress_image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )

    # Field to store the date and time when the progress picture was uploaded.
    # Automatically set to the current date
    # and time when the record is created.
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the progress picture entry,
        # including the username and the upload date.
        return f"{self.user.user.username} - {self.uploaded_at}"
