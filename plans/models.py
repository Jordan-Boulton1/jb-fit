from django.db import models

# Create your models here.


class TrainingPlan(models.Model):
    """
    Model representing a training plan with a name, description, price,
    and creation timestamp.
    """

    # Name of the training plan with a max length of 100 characters
    name = models.CharField(max_length=100)

    # Detailed description of the training plan
    description = models.TextField()

    # Price of the training plan, with up to 5 digits and 2 decimal places
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Timestamp of when the training plan was created, set automatically
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the TrainingPlan object, returning the name.
        """
        return self.name
