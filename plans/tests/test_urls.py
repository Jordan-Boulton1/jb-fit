from django.test import SimpleTestCase
from django.urls import reverse, resolve
from plans.views import plans


class PlansUrlsTest(SimpleTestCase):
    """
    Test case for verifying the URL resolution of the plans view.
    """

    def test_plans_url_is_resolved(self):
        """
        Tests if the URL named 'plans' correctly resolves to the plans view.
        """
        # Use reverse to get the URL for the 'plans' view
        url = reverse('plans')

        # Check if resolving the URL returns the correct view function
        self.assertEqual(resolve(url).func, plans)
