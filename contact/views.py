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
            
            messages.success(request, 'Your message has been sent and saved successfully.')
            return redirect('home')  # Redirect to home or any other page after submission
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
