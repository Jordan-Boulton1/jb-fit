from django.test import SimpleTestCase
from django.urls import reverse, resolve
from faq.views import faq


class FaqUrlsTest(SimpleTestCase):

    def test_faq_url_is_resolved(self):
        url = reverse('faq')
        self.assertEqual(resolve(url).func, faq)
