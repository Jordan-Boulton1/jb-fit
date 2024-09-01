from django.test import SimpleTestCase
from django.urls import reverse, resolve
from faq.views import faq


class FaqUrlsTest(SimpleTestCase):
    """
    Test case for verifying the FAQ URL resolution.
    """

    def test_faq_url_is_resolved(self):
        """
        Tests if the URL named 'faq' correctly resolves to the faq view.
        """
        # Use reverse to get the URL for the 'faq' view
        url = reverse('faq')

        # Check if resolving the URL returns the correct view function
        self.assertEqual(resolve(url).func, faq)
