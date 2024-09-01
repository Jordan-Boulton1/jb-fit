from .forms import NewsletterForm
from django.contrib import messages


def newsletter_form(request):
    """
    Handles the newsletter form submission,
    validating input and providing feedback messages to the user.

    :param request: HttpRequest object representing the client request.
    :return: Dictionary containing the newsletter form to be used
    in the context.
    """
    # Initialize an empty NewsletterForm instance
    form = NewsletterForm()

    # Check if the request is a POST and the form_type is 'newsletter'
    if (
        request.method == 'POST' and
        request.POST.get('form_type') == 'newsletter'
    ):
        # Populate the form with POST data
        form = NewsletterForm(request.POST)

        # Validate the form
        if form.is_valid():
            # Save the form data to create a new Newsletter instance
            form.save()

            # Add a success message for the user
            messages.success(
                request,
                'Successfully subscribed to the newsletter!',
                extra_tags='newsletter'
            )
        else:
            # Iterate over form errors and add each error message for the user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request,
                        f"{field.capitalize()}: {error}",
                        extra_tags='newsletter'
                    )

    # Return the form in the context dictionary, whether valid or not
    return {'newsletter_form': form}
