# Import the forms module from Django
from django import forms


# Define a ContactForm class inheriting from Django's base Form class
class ContactForm(forms.Form):
    # Define a CharField for the first name with specific attributes
    first_name = forms.CharField(
        max_length=50,  # Set the maximum length of the first name
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'required': 'required',
            'id': 'contact_first_name'
        })
    )

    # Define a CharField for the last name with specific attributes
    last_name = forms.CharField(
        max_length=50,  # Set the maximum length of the last name
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'required': 'required',
            'id': 'contact_last_name'
        })
    )

    # Define an EmailField for the email address with specific attributes
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'required': 'required',
            'id': 'contact_email'
        })
    )

    # Define a CharField for the message with
    # a Textarea widget and specific attributes
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Your Message',
            'required': 'required',
            'id': 'contact_message'
        })
    )
