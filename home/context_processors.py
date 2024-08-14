from .forms import NewsletterForm
from django.contrib import messages

def newsletter_form(request):
    form = NewsletterForm()
    
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed to the newsletter!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    # Always return the form in the context dictionary
    return {'newsletter_form': form}
