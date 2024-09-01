from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter, based on the Newsletter model.
    """

    class Meta:
        # Specifies the model to be used for this form
        model = Newsletter

        # Defines the fields from the model to include in the form
        fields = ['email']

        # Customizes the widget for the email field
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',       # Adds CSS class for styling
                'placeholder': 'Email address',  # Sets placeholder text
                'id': 'newsletter_email'        # Sets the ID attribute
            }),
        }
