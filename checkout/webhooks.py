import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from checkout.models import Order

@csrf_exempt
def stripe_webhook(request):
    """Listen for webhooks from stripe"""
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    try:
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            order = Order.objects.get(stripe_payment_intent_id=payment_intent['id'])
            order.paid = True
            order.save()

            __send_confirmation_email(order)

    except Order.DoesNotExist:
        return "Order not found."

    return HttpResponse(status=200)



def __send_confirmation_email(order):
    """Send a confirmation email to the user"""
    subject = render_to_string(
        'checkout/emails/confirmation_email_subject.txt'
    ).strip()
    message = render_to_string(
        'checkout/emails/confirmation_email_body.txt',
        {
            'first_name': order.first_name,
            'training_plan': order.training_plan.name,
            'amount': order.amount,
            'order_date': order.created_at.strftime('%B %d, %Y'),
        }
    )
    recipient = order.email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient],
        fail_silently=False,
    )
