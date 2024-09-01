from django.shortcuts import render
from checkout.models import Order
from .models import TrainingPlan

# Create your views here.


def plans(request):
    """
    Handles the request for the plans page and returns the rendered template.

    Retrieves all training plans and checks if the authenticated user has
    ordered any plans, passing this information to the template.

    :param request: HttpRequest object representing the client request.
    :return: HttpResponse object with the rendered plans page.
    """
    # Retrieve all training plans from the database
    plans = TrainingPlan.objects.all()

    # Initialize an empty list for training plan IDs that the user has ordered
    user_ordered_plan_ids = []

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the training plan IDs from the user's orders
        user_ordered_plan_ids = Order.objects.filter(
            user=request.user
        ).values_list('training_plan_id', flat=True)

    # Render the plans page with the retrieved training plans and user's orders
    return render(request, "plans/plans.html", {
        'plans': plans,
        'user_ordered_plan_ids': user_ordered_plan_ids,
    })
