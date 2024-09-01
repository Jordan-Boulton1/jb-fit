# Import necessary modules and classes for testing
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import contact_coach


# Define test cases for URL resolution
class TestUrls(SimpleTestCase):

    # Test case for checking if the 'contact_coach' URL resolves correctly
    def test_contact_coach_url_is_resolved(self):
        # Use reverse to get the URL pattern for the name 'contact_coach'
        url = reverse('contact_coach')

        # Use resolve to match the URL pattern to a view function
        self.assertEqual(resolve(url).func, contact_coach)
