from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'First Name', 
        'required': 'required',
        'id': 'contact_first_name'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Last Name', 
        'required': 'required',
        'id': 'contact_last_name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Email Address', 
        'required': 'required',
        'id': 'contact_email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'rows': 5, 
        'placeholder': 'Your Message', 
        'required': 'required',
        'id': 'contact_message'
    }))