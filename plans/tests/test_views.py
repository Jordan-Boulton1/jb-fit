from django.test import TestCase
from django.urls import reverse

class PlansViewTest(TestCase):

    def test_plans_view(self):
        response = self.client.get(reverse('plans'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plans/plans.html')
