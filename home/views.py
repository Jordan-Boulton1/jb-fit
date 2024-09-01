from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Handles the request for the home page and returns the rendered template.

    :param request: HttpRequest object representing the client request.
    :return: HttpResponse object with the rendered home page.
    """
    # Render the 'home/home.html' template and return the response
    return render(request, "home/home.html")
