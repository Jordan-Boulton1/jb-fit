from django.test import TestCase
from django.urls import reverse


class AboutViewTest(TestCase):

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
