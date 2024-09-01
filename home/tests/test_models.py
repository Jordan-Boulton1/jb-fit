from django.test import TestCase
from home.models import Newsletter


class NewsletterModelTest(TestCase):
    """
    Test case for the Newsletter model to ensure it works as expected.
    """

    def test_newsletter_creation(self):
        """
        Tests the creation of a Newsletter instance
        and its string representation.
        """
        # Create a Newsletter instance with a test email
        newsletter = Newsletter.objects.create(email='test@example.com')

        # Assert that the string representation of the instance is the email
        self.assertEqual(str(newsletter), 'test@example.com')

        # Assert that the email attribute is correctly set
        self.assertEqual(newsletter.email, 'test@example.com')
