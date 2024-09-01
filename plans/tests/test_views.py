from django.test import TestCase
from django.urls import reverse


class PlansViewTest(TestCase):
    """
    Test case for the plans view to ensure it loads correctly.
    """

    def test_plans_view(self):
        """
        Tests the plans view for correct status code and template usage.
        """
        # Make a GET request to the 'plans' URL
        response = self.client.get(reverse('plans'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'plans/plans.html')
