from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home

class HomeUrlsTest(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
