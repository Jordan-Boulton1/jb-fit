from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_email(self):
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'message': 'This is a test message.',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_contact_form_missing_field(self):
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': '',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)
