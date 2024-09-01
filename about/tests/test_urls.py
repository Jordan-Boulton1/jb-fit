from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import about


# Define a test case class for testing URLs in the 'about' app.
class AboutUrlsTest(SimpleTestCase):
    """
    This test case checks that the URL configuration for the 'about' view
    is correctly set up and resolves to the expected view function.
    """

    def test_about_url_is_resolved(self):
        """
        Tests that the 'about' URL
        correctly resolves to the 'about' view function.

        This test uses the 'reverse' function to get the URL for the 'about'
        view by its name, and then uses 'resolve' to ensure that the URL
        matches the expected view function.
        """
        # Use 'reverse' to get the URL path from the 'about' view name.
        url = reverse('about')

        # Check that resolving this URL path returns the correct view function.
        self.assertEqual(
            resolve(url).func,
            about
        )
