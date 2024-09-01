# Import the necessary modules and classes
import re  # For regular expressions to validate phone number format
from django import forms  # Django forms module for creating forms
from .models import Order
from django.core.exceptions import ValidationError


# Define a form class for the Order model using ModelForm
class OrderForm(forms.ModelForm):
    class Meta:
        # Specify the model associated with the form
        model = Order
        # Define the fields that will be included in the form
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    # Initialize the form and customize field attributes
    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super(OrderForm, self).__init__(*args, **kwargs)
        # Remove the default colon suffix from labels
        self.label_suffix = ''
        # Iterate through each field in the form
        for field in self.fields:
            # Update widget attributes to add
            # Bootstrap styling and set fields as required
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': True  # Set each field as required
            })

    # Custom validation method for the first name field
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        # Check if the first name contains only alphabetic characters
        if not first_name.isalpha():
            raise ValidationError(
                'First name should only contain alphabetic characters.'
            )
        return first_name  # Return the cleaned value if valid

    # Custom validation method for the last name field
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        # Check if the last name contains only alphabetic characters
        if not last_name.isalpha():
            raise ValidationError(
                'Last name should only contain alphabetic characters.'
            )
        return last_name  # Return the cleaned value if valid

    # Custom validation method for the phone number field
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Check if the phone number contains
        # only numeric characters using regex
        if not re.fullmatch(r'\d+', phone_number):
            raise ValidationError(
                'Phone number should only contain numeric characters.'
            )
        return phone_number  # Return the cleaned value if valid
