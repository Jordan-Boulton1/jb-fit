# Import the models module from Django
from django.db import models

# Define your models here


# Define a model for storing contact form submissions
class ContactSubmission(models.Model):
    # Field for storing the first name of the contact
    first_name = models.CharField(max_length=50)

    # Field for storing the last name of the contact
    last_name = models.CharField(max_length=50)

    # Field for storing the email address of the contact
    email = models.EmailField()

    # Field for storing the message submitted by the contact
    message = models.TextField()

    # Field for storing the timestamp when the submission was created
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Define a string representation for the model,
    # useful in admin interfaces and debugging
    def __str__(self):
        # Returns a string combining the first name,
        # last name, and email of the contact
        return f'{self.first_name} {self.last_name} - {self.email}'
