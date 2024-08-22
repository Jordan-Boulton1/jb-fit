from django.test import TestCase
from django.urls import reverse

class FaqViewTest(TestCase):

    def test_faq_view(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/faq.html')
