from django.shortcuts import render

# Create your views here.


def home(request):
    """Returns the rendered home page."""
    return render(request, "home/home.html")
