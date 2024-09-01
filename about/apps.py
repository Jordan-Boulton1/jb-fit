from django.apps import AppConfig


# Define a configuration class for the 'about' application.
class AboutConfig(AppConfig):
    # Sets the default type of primary key to be used for models in this app.
    # 'BigAutoField' is a 64-bit integer, which provides a larger range
    # than the default 'AutoField'.
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifies the name of the application.
    # This should match the name of the application folder or the label
    # used in Django settings.
    name = 'about'
