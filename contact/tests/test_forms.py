# Import necessary modules and classes for testing
from django.test import TestCase
from contact.forms import ContactForm


# Define test cases for the ContactForm
class ContactFormTest(TestCase):

    # Test case for a valid form submission
    def test_contact_form_valid_data(self):
        # Create a form instance with valid data
        form = ContactForm(data={
            'first_name': 'John',  # Valid first name
            'last_name': 'Doe',    # Valid last name
            'email': 'john.doe@example.com',  # Valid email
            'message': 'This is a test message.',  # Valid message content
        })

        # Check that the form is valid
        self.assertTrue(form.is_valid())

    # Test case for an invalid email address
    def test_contact_form_invalid_email(self):
        # Create a form instance with an invalid email address
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',  # Invalid email format
            'message': 'This is a test message.',
        })

        # Check that the form is invalid
        self.assertFalse(form.is_valid())
        # Check that the 'email' field is in the form's error dictionary
        self.assertIn('email', form.errors)

    # Test case for a missing required field
    def test_contact_form_missing_field(self):
        # Create a form instance with a missing last name
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': '',  # Missing last name (required field)
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        # Check that the form is invalid
        self.assertFalse(form.is_valid())
        # Check that the 'last_name' field is in the form's error dictionary
        self.assertIn('last_name', form.errors)
