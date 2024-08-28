from django.shortcuts import render
from .models import TrainingPlan

# Create your views here.


def plans(request):
    """Returns the rendered plans page."""
    plans = TrainingPlan.objects.all()
    return render(request, "plans/plans.html", {'plans': plans})
