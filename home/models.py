from django.db import models

# Create your models here.


class Newsletter(models.Model):
    """
    Model representing a subscription to the newsletter with an email address.
    """

    # Email field with a unique constraint to prevent duplicate subscriptions
    email = models.EmailField(unique=True)

    # DateTime field that automatically sets the current timestamp on creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Newsletter object, returning the email.
        """
        return self.email
