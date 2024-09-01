from django.shortcuts import render


# Create your views here.


def about(request):
    """
    Handles the request to display the about page.

    This view function receives an HTTP request object and returns
    an HTTP response object with the rendered 'about' page template.

    Args:
        request: The HTTP request object provided by Django, containing
                metadata about the request made by the client.

    Returns:
        HttpResponse: A response object that renders the 'about.html' template
                    located in the 'about' directory.
    """
    # Renders the 'about.html' template and returns it as an HTTP response.
    # The 'render' function combines the template with a context dictionary
    # (if provided) and the HTTP request to produce the final HTML content.
    return render(request, "about/about.html")
