from django.test import TestCase
from home.forms import NewsletterForm
from home.models import Newsletter


class NewsletterFormTest(TestCase):
    """
    Test case for the NewsletterForm to ensure it behaves as expected.
    """

    def test_newsletter_form_valid_data(self):
        """
        Tests that the form is valid when provided with correct data.
        """
        # Create a form instance with valid email data
        form = NewsletterForm(data={'email': 'test@example.com'})

        # Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_newsletter_form_invalid_email(self):
        """
        Tests that the form is invalid when given an incorrect email format.
        """
        # Create a form instance with an invalid email format
        form = NewsletterForm(data={'email': 'not-an-email'})

        # Assert that the form is invalid
        self.assertFalse(form.is_valid())

        # Check that the 'email' field is in the form errors
        self.assertIn('email', form.errors)

    def test_newsletter_form_missing_email(self):
        """
        Tests that the form is invalid when the email field is empty.
        """
        # Create a form instance with missing email data
        form = NewsletterForm(data={'email': ''})

        # Assert that the form is invalid
        self.assertFalse(form.is_valid())

        # Check that the 'email' field is in the form errors
        self.assertIn('email', form.errors)
