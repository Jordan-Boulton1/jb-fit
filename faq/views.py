from django.shortcuts import render

# Create your views here.


def faq(request):
    """Returns the rendered faq page."""
    return render(request, "faq/faq.html")
