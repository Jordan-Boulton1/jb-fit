# Import the ContactForm class from the forms module within the current app
from .forms import ContactForm


# Define a function to provide the contact form with initial data
def contact_form(request):
    # Initialize an empty dictionary for initial form data
    initial_data = {}

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If the user is logged in, populate
        # initial data with the user's information
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }

    # Create an instance of the ContactForm, passing in the initial data
    form = ContactForm(initial=initial_data)

    # Return the form instance in a context dictionary to be used in templates
    return {'contact_form': form}
