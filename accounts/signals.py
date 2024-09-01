from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages


# Define a signal receiver function to handle the user_logged_in signal.
# This function is triggered whenever a user logs in successfully.
@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    """
    Signal receiver function that is called when a user logs in.

    Args:
        sender: The model class that sent the signal.
        request: The HTTP request object that triggered the login.
        user: The user instance that just logged in.
        **kwargs: Additional keyword arguments passed by the signal.

    This function adds a success message to the request, welcoming the user
    by their first name. If the first name is not available, it defaults
    to using the username.
    """
    # Retrieve the first name of the logged-in user.
    # If the first name is empty, it defaults to the username.
    first_name = user.first_name

    # Add a success message to the request using Django's messaging framework.
    # This message is displayed to the user after they log in.
    messages.success(request, f"Welcome, {first_name}!")
