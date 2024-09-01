# Import the path function for defining URL patterns
from django.urls import path

# Import the view function to be used in the URL pattern
from .views import contact_coach

# Define the URL patterns for the app
urlpatterns = [
    # Define a URL pattern for the contact_coach view
    path('', contact_coach, name='contact_coach'),

    # The name 'contact_coach' allows this URL pattern
    # to be referenced by name in templates and views,
    # making it easier to manage links and redirects within the application
]
