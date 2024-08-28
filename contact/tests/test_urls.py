from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import contact_coach


class TestUrls(SimpleTestCase):

    def test_contact_coach_url_is_resolved(self):
        url = reverse('contact_coach')
        self.assertEqual(resolve(url).func, contact_coach)
