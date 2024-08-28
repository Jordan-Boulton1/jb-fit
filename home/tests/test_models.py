from django.test import TestCase
from home.models import Newsletter


class NewsletterModelTest(TestCase):

    def test_newsletter_creation(self):
        newsletter = Newsletter.objects.create(email='test@example.com')
        self.assertEqual(str(newsletter), 'test@example.com')
        self.assertEqual(newsletter.email, 'test@example.com')
