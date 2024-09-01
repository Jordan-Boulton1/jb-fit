from django.apps import AppConfig


# Define the configuration class for the 'accounts' application.
class AccountsConfig(AppConfig):
    # Sets the default type of primary key for models in this app.
    # 'BigAutoField' is a 64-bit integer, providing a larger range
    # than 'AutoField'.
    default_auto_field = 'django.db.models.BigAutoField'

    # Specifies the name of the application.
    # This should match the directory name of the app or the label
    # used in Django settings.
    name = 'accounts'

    def ready(self):
        """
        This method is called when the application is ready.

        The 'ready' method is used to perform application-specific
        initialization tasks, such as registering signals. In this case,
        it imports the signals module from the 'accounts' app, ensuring
        that signal handlers are connected when the app is loaded.
        """
        # Import the signals module to connect signal handlers when the
        # app is loaded. This ensures that signals are registered and
        # ready to be used throughout the application.
        import accounts.signals
