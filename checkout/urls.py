# Import necessary modules and functions for URL configuration
from django.urls import path  # Import path function for defining URL patterns
from . import views  # Import views from the current app
from .webhooks import stripe_webhook

# Define URL patterns for the app
urlpatterns = [
    # URL pattern for the checkout view
    # Expects an integer plan_id as part of the URL
    # Directs to the 'checkout' view function in views.py
    path(
        'checkout/<int:plan_id>/',  # URL pattern with a plan_id parameter
        views.checkout,  # View function to handle the checkout process
        name='checkout'  # Name of the URL pattern for reverse lookup
    ),

    # URL pattern for the checkout success view
    # Expects an integer order_id as part of the URL
    # Directs to the 'checkout_success' view function in views.py
    path(
        'success/<int:order_id>',  # URL pattern with an order_id parameter
        views.checkout_success,  # View function to handle successful checkouts
        name='checkout_success'  # Name of the URL pattern for reverse lookup
    ),

    # URL pattern for handling Stripe webhooks
    # Directs to the 'stripe_webhook' function in webhooks.py
    path(
        'checkout/webhook',  # URL for receiving webhook events from Stripe
        stripe_webhook,  # Function to handle Stripe webhook events
        name='stripe_webhook'  # Name of the URL pattern for reverse lookup
    ),
]
