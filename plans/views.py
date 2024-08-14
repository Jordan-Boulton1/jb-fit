from django.shortcuts import render

# Create your views here.

def plans(request):
    """Returns the rendered plans page."""
    return render(request, "plans/plans.html")
