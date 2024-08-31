from .forms import ContactForm


def contact_form(request):
    initial_data = {}
    # Check if user is authenticated and form is requested
    if request.user.is_authenticated:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
    form = ContactForm(initial=initial_data)
    return {'contact_form': form}
