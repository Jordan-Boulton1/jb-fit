# Import the AppConfig class from the django.apps module
from django.apps import AppConfig


# Define a configuration class for the 'contact' app
class ContactConfig(AppConfig):
    # Set the default type of auto-generated
    # primary keys for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the application as it appears in the Django project
    name = 'contact'
