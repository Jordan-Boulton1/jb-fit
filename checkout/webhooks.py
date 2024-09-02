# Import necessary modules and functions
import stripe  # Stripe API for handling payment-related events
from django.http import HttpResponse  # For sending HTTP responses
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # For accessing project settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage  # For sending emails
from checkout.models import Order  # Import the Order model


# Define a view to handle Stripe webhooks
@csrf_exempt  # Exempt this view from CSRF protection
# as it receives requests from external sources
def stripe_webhook(request):
    """Listen for webhooks from Stripe"""
    # Get the webhook payload and Stripe signature header from the request
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None  # Initialize the event variable

    try:
        # Construct the event using Stripe's helper
        # method and verify the signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # If the payload is invalid, return a 400 Bad Request response
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # If the signature verification fails,
        # return a 400 Bad Request response
        return HttpResponse(status=400)

    # Handle the event based on its type
    try:
        if event['type'] == 'payment_intent.succeeded':
            # If the payment was successful, retrieve the payment intent object
            payment_intent = event['data']['object']
            # Find the corresponding order using the Stripe payment intent ID
            order = Order.objects.get(
                stripe_payment_intent_id=payment_intent['id']
            )
            # Mark the order as paid
            order.paid = True
            order.save()  # Save the changes to the database

            # Send a confirmation email to the user
            __send_confirmation_email(order)

    except Order.DoesNotExist:
        # If the order does not exist, return a 404 Not Found response
        return HttpResponse("Order not found.", status=404)

    # Return a 200 OK response to acknowledge receipt of the event
    return HttpResponse(status=200)


# Private function to send a confirmation email to the user
def __send_confirmation_email(order):
    """Send a confirmation email to the user"""

    # Render the subject of the email from a template
    # and strip extra whitespace
    subject = render_to_string(
        'checkout/emails/confirmation_email_subject.txt'
    ).strip()

    # Render the HTML body of the email using a template
    # and pass order details as context
    html_content = render_to_string(
        'checkout/emails/confirmation_email_body.html',
        {
            'first_name': order.first_name,
            'training_plan': order.training_plan.name,
            'amount': order.amount,
            'order_date': order.created_at.strftime('%B %d, %Y'),
        }
    )

    # Get the recipient email address from the order
    recipient = order.email

    # Create the email object with the HTML content
    email = EmailMessage(
        subject=subject,  # Email subject
        body=html_content,  # HTML content of the email
        from_email=settings.DEFAULT_FROM_EMAIL,  # Sender's email address
        to=[recipient],  # List of recipient email addresses
    )

    # Set the content type to HTML
    email.content_subtype = "html"

    # Send the email
    email.send(fail_silently=False)  # Raise an exception if sending fails
