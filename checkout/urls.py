from django.urls import path
from . import views
from .webhooks import stripe_webhook

urlpatterns = [
    path(
        'checkout/<int:plan_id>/',
        views.checkout,
        name='checkout'
    ),
    path(
        'success/<int:order_id>',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'checkout/webhook',
        stripe_webhook,
        name='stripe_webhook'
    ),
]
