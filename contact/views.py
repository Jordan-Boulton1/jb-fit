from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactSubmission


def contact_coach(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            ContactSubmission.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            messages.success(
                request,
                'Your message has been sent and saved successfully.',
                extra_tags='contact'
            )
            # Redirect to home or any other page after submission
            return redirect('home')
    else:
        for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}",
                    extra_tags='contact')

    return render(request, 'contact/contact_form.html', {'form': form})
