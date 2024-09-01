from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home


class HomeUrlsTest(SimpleTestCase):
    """
    Test case for verifying the URL resolution of the home view.
    """

    def test_home_url_is_resolved(self):
        """
        Tests if the URL named 'home' correctly resolves to the home view.
        """
        # Use reverse to get the URL for the 'home' view
        url = reverse('home')

        # Check if resolving the URL returns the correct view function
        self.assertEqual(resolve(url).func, home)
