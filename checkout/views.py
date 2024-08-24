from django.urls import reverse
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.contrib import messages
from .models import TrainingPlan

# Create your views here.
@login_required
def checkout(request, plan_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    training_plan = get_object_or_404(TrainingPlan, id=plan_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                order = form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.user = request.user
                order.training_plan = training_plan
                order.amount = training_plan.price
                order.stripe_payment_intent_id = pid
                order.save()

                print(order)
                stripe.PaymentIntent.modify(pid,  metadata={'order_id': order.id})

                return redirect(reverse('checkout_success', args=[order.id]))
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('checkout', plan_id=plan_id)
        else:
            messages.error(request, "Form is invalid. Please check the details.")
            return redirect('checkout', plan_id=plan_id)
    else:
        # Handle GET request
        form = OrderForm()
        stripe.api_key = stripe_secret_key
        # Create PaymentIntent with metadata
        intent = stripe.PaymentIntent.create(
            amount=int(training_plan.price * 100),
            currency='gbp'
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': form,
        'training_plan': training_plan,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)



from .models import Order

@login_required
def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
