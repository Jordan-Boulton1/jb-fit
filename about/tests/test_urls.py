from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import about

class AboutUrlsTest(SimpleTestCase):

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
