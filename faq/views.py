from django.shortcuts import render

# Create your views here.


def faq(request):
    """
    Handles the FAQ view and returns the rendered FAQ page.

    :param request: HttpRequest object representing the client request.
    :return: HttpResponse object with the rendered FAQ page and context.
    """
    # Render the FAQ template with the given context.
    return render(request, "faq/faq.html", context)
