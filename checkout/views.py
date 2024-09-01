# Import necessary modules and functions
from django.urls import reverse  # For URL resolution in redirects
import stripe  # Stripe API for payment processing
from django.conf import settings  # For accessing project settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile  # Import UserProfile model
from .forms import OrderForm  # Import the OrderForm for order creation
from django.contrib import messages  # For displaying messages to the user
from .models import TrainingPlan, Order  # Import TrainingPlan and Order models

# Define your views here


# View function for the checkout process
@login_required  # Ensure the user is logged in to access this view
def checkout(request, plan_id):
    # Retrieve Stripe keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key  # Set the Stripe API key

    # Fetch the training plan based on the provided plan_id
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)

    # Handle form submission when the request method is POST
    if request.method == 'POST':
        form = OrderForm(request.POST)  # Create form instance with POST data
        if form.is_valid():  # Check if the form data is valid
            try:
                order = form.save(commit=False)
                # Extract payment intent ID from
                # the client secret provided by Stripe
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.user = request.user
                order.training_plan = training_plan
                order.amount = training_plan.price
                order.stripe_payment_intent_id = pid
                order.save()  # Save the order to the database

                # Modify the Stripe payment intent
                # to include the order ID in its metadata
                stripe.PaymentIntent.modify(
                    pid, metadata={'order_id': order.id}
                )

                # Redirect to the checkout success page after saving the order
                return redirect(reverse('checkout_success', args=[order.id]))
            except Exception as e:
                # If an error occurs, display an error message
                # and redirect back to the checkout page
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('checkout', plan_id=plan_id)
        else:
            # If the form is invalid, display each form error as a message
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            return redirect('checkout', plan_id=plan_id)
    else:
        # Handle GET request to display the checkout page
        try:
            # Attempt to pre-fill the form with the user's profile data
            profile = UserProfile.objects.get(user=request.user)
            form = OrderForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone_number': profile.phone_number or ''
            })
        except UserProfile.DoesNotExist:
            # If the user profile does not exist, initialize an empty form
            form = OrderForm()

        # Create a new Stripe payment intent for the order amount
        intent = stripe.PaymentIntent.create(
            amount=int(training_plan.price * 100),  # Amount in cents
            currency='gbp'  # Currency set to GBP
        )

    # Check if the Stripe public key is missing and display a warning message
    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing. Did you forget to set it '
            'in your environment?'
        )

    # Define the template and context for rendering the checkout page
    template = 'checkout/checkout.html'
    context = {
        'order_form': form,  # The order form instance
        'training_plan': training_plan,  # The selected training plan
        'stripe_public_key': stripe_public_key,
        'client_secret': intent['client_secret'],
    }

    # Render the checkout template with the provided context
    return render(request, template, context)


# View function for handling successful checkout
@login_required  # Ensure the user is logged in to access this view
def checkout_success(request, order_id):
    # Fetch the order based on the provided order_id
    # and ensure it belongs to the current user
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Define the template and context for rendering the checkout success page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,  # The order instance to display
    }

    # Render the checkout success template with the provided context
    return render(request, template, context)
