# Import the AppConfig class from django.apps module
from django.apps import AppConfig


# Define a configuration class for the 'checkout' app
class CheckoutConfig(AppConfig):
    # Set the default auto field type for primary keys in models
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the app this configuration is for
    name = 'checkout'
