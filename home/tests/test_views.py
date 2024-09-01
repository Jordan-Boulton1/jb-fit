from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    """
    Test case for the home view to ensure it loads correctly.
    """

    def test_home_view(self):
        """
        Tests the home view for correct status code and template usage.
        """
        # Make a GET request to the 'home' URL
        response = self.client.get(reverse('home'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'home/home.html')
