from django.shortcuts import render

# Create your views here.


def about(request):
    """Returns the rendered about page."""
    return render(request, "about/about.html")
