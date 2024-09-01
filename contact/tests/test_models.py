# Import necessary modules and classes for testing
from django.test import TestCase
from contact.models import ContactSubmission


# Define test cases for the ContactSubmission model
class ContactSubmissionModelTest(TestCase):

    # Test case for creating a ContactSubmission instance
    def test_contact_submission_creation(self):
        # Create a ContactSubmission instance with valid data
        submission = ContactSubmission.objects.create(
            first_name='John',  # Set the first name
            last_name='Doe',    # Set the last name
            email='john.doe@example.com',  # Set the email address
            message='This is a test message.'  # Set the message content
        )

        # Check the string representation of the submission instance
        self.assertEqual(str(submission), 'John Doe - john.doe@example.com')
        # Verify that the first name is correctly saved
        self.assertEqual(submission.first_name, 'John')
        # Verify that the last name is correctly saved
        self.assertEqual(submission.last_name, 'Doe')
        # Verify that the email is correctly saved
        self.assertEqual(submission.email, 'john.doe@example.com')
        # Verify that the message is correctly saved
        self.assertEqual(submission.message, 'This is a test message.')
