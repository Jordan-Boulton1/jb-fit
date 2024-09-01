import re
from django import forms
from .models import Order
from django.core.exceptions import ValidationError


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': True
            })

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError(
                'First name should only contain alphabetic characters.'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError(
                'Last name should only contain alphabetic characters.'
            )
        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.fullmatch(r'\d+', phone_number):
            raise ValidationError(
                'Phone number should only contain numeric characters.'
            )
        return phone_number
