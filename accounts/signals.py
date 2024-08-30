from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    # Use the first name of the user in the success message
    first_name = user.first_name  # Fallback to username if first name is empty
    messages.success(request, f"Welcome, {first_name}!")
