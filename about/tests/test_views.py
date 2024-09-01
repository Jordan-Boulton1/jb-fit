from django.test import TestCase
from django.urls import reverse


# Define a test case class for testing the 'about' view.
class AboutViewTest(TestCase):
    """
    This test case checks the behavior of the 'about' view to ensure it
    returns the correct status code and uses the appropriate template.
    """

    def test_about_view(self):
        """
        Tests the 'about' view's response and template usage.

        This test sends a GET request to the 'about' URL and checks that:
        1. The HTTP response status code is 200 (OK), indicating that the
        page was successfully rendered.
        2. The response uses the 'about/about.html' template, verifying that
        the correct template is being used for the 'about' view.
        """
        # Send a GET request to the 'about' view using the reverse URL lookup.
        response = self.client.get(reverse('about'))

        # Assert that the response status code is 200, indicating success.
        self.assertEqual(response.status_code, 200)

        # Assert that the response uses the 'about/about.html' template.
        self.assertTemplateUsed(response, 'about/about.html')
