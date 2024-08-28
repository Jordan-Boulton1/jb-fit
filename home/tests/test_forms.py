from django.test import TestCase
from home.forms import NewsletterForm
from home.models import Newsletter


class NewsletterFormTest(TestCase):

    def test_newsletter_form_valid_data(self):
        form = NewsletterForm(data={'email': 'test@example.com'})
        self.assertTrue(form.is_valid())

    def test_newsletter_form_invalid_email(self):
        form = NewsletterForm(data={'email': 'not-an-email'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_newsletter_form_missing_email(self):
        form = NewsletterForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
