from django.test import SimpleTestCase
from django.urls import reverse, resolve
from plans.views import plans


class PlansUrlsTest(SimpleTestCase):

    def test_plans_url_is_resolved(self):
        url = reverse('plans')
        self.assertEqual(resolve(url).func, plans)
