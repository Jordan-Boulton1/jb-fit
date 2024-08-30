from .forms import NewsletterForm
from django.contrib import messages


def newsletter_form(request):
    print(request)
    form = NewsletterForm()

    if (
        request.method == 'POST' and
        request.POST.get('form_type') == 'newsletter'
    ):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Successfully subscribed to the newsletter!',
                extra_tags='newsletter'
            )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}",
                    extra_tags='newsletter')

    # Always return the form in the context dictionary
    return {'newsletter_form': form}
