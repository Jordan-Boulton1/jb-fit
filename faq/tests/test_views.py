from django.test import TestCase
from django.urls import reverse


class FaqViewTest(TestCase):
    """
    Test case for the FAQ view to ensure it loads correctly.
    """

    def test_faq_view(self):
        """
        Tests the FAQ view for correct status code and template usage.
        """
        # Make a GET request to the 'faq' URL
        response = self.client.get(reverse('faq'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'faq/faq.html')
