# Import necessary modules and functions
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactSubmission


# Define the view function for handling contact form submissions
def contact_coach(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = ContactForm(request.POST)

        # Validate the form data
        if form.is_valid():
            # Save form data to the database by creating
            # a new ContactSubmission instance
            ContactSubmission.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Display a success message to the user
            messages.success(
                request,
                'Your message has been sent and saved successfully.',
                extra_tags='contact'
            )
            
            # Redirect back to the referring page using the 'next' parameter
            # Default to 'home' if 'next' is not present
            next_url = request.POST.get('next', 'home') 
            return redirect(next_url)
        else:
            # Handle form errors if the form is not valid
            # Iterate through each field and its errors
            for field, errors in form.errors.items():
                for error in errors:
                    # Display each error message to the user
                    messages.error(
                        request,
                        f"{field.capitalize()}: {error}",
                        extra_tags='contact'
                    )

    # Render the contact form template if the request
    # method is not POST or if the form is invalid
    return render(request, 'contact/contact_form.html')
