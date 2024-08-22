from django.test import TestCase
from django.urls import reverse
from contact.models import ContactSubmission
from contact.forms import ContactForm

class ContactViewTest(TestCase):

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact_coach'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid_data(self):
        response = self.client.post(reverse('contact_coach'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        self.assertEqual(response.status_code, 302)  # Check for a redirect
        self.assertRedirects(response, reverse('home'))

        # Check that the message was saved to the database
        self.assertTrue(ContactSubmission.objects.filter(email='john.doe@example.com').exists())

    def test_contact_view_post_invalid_data(self):
        response = self.client.post(reverse('contact_coach'), {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')
        self.assertFalse(ContactSubmission.objects.exists())  # Ensure nothing was saved