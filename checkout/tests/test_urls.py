from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout import views
from checkout.webhooks import stripe_webhook

class CheckoutURLsTestCase(SimpleTestCase):

    def test_checkout_url_resolves(self):
        """Test that the checkout URL resolves correctly."""
        url = reverse('checkout', args=[1])  # Plan ID = 1
        self.assertEqual(resolve(url).func, views.checkout)

    def test_checkout_success_url_resolves(self):
        """Test that the checkout success URL resolves correctly."""
        url = reverse('checkout_success', args=[1])  # Order ID = 1
        self.assertEqual(resolve(url).func, views.checkout_success)

    def test_stripe_webhook_url_resolves(self):
        """Test that the stripe webhook URL resolves correctly."""
        url = reverse('stripe_webhook')
        self.assertEqual(resolve(url).func, stripe_webhook)

    def test_reverse_checkout_url(self):
        """Test reverse lookup of checkout URL."""
        url = reverse('checkout', args=[1])
        self.assertEqual(url, '/checkout/1/')  # Expected path

    def test_reverse_checkout_success_url(self):
        """Test reverse lookup of checkout success URL."""
        url = reverse('checkout_success', args=[1])
        self.assertEqual(url, '/success/1')  # Expected path

    def test_reverse_stripe_webhook_url(self):
        """Test reverse lookup of stripe webhook URL."""
        url = reverse('stripe_webhook')
        self.assertEqual(url, '/checkout/webhook')  # Expected path
