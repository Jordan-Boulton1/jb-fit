# Import necessary modules and classes for testing
from django.test import TestCase
from django.urls import reverse
from contact.models import ContactSubmission
from contact.forms import ContactForm


# Define test cases for the contact view
class ContactViewTest(TestCase):

    # Test the GET request to the contact view
    def test_contact_view_get(self):
        # Simulate a GET request to the 'contact_coach' URL
        response = self.client.get(reverse('contact_coach'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'contact/contact_form.html')

        # Check that the context contains an instance of ContactForm
        self.assertIsInstance(response.context['form'], ContactForm)

    # Test the POST request to the contact view with valid data
    def test_contact_view_post_valid_data(self):
        # Simulate a POST request to the 'contact_coach'
        # URL with valid form data
        response = self.client.post(reverse('contact_coach'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        # Check that the response status code is 302 (indicating a redirect)
        self.assertEqual(response.status_code, 302)

        # Verify that the response redirects to the 'home' URL
        self.assertRedirects(response, reverse('home'))

        # Check that the contact submission was saved to the database
        self.assertTrue(
            ContactSubmission.objects.filter(
                email='john.doe@example.com'
            ).exists()
        )

    # Test the POST request to the contact view with invalid data
    def test_contact_view_post_invalid_data(self):
        # Simulate a POST request to the 'contact_coach'
        # URL with invalid form data (missing first name)
        response = self.client.post(reverse('contact_coach'), {
            'first_name': '',  # Invalid: first name is required but empty
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message.',
        })

        # Check that the response status code is 200
        # (form errors should re-render the page)
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, 'contact/contact_form.html')

        # Check that no submissions were saved to the
        # database due to the invalid form data
        self.assertFalse(ContactSubmission.objects.exists())
