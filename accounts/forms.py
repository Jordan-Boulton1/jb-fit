from allauth.account.forms import SignupForm
from django import forms

from accounts.models import UserProfile


class CustomSignupForm(SignupForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'required': 'true'}
        )
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'required': 'true'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        gender_map = {
            'M': 'Male',
            'F': 'Female',
            'O': 'Other'
        }
        full_gender = gender_map.get(self.cleaned_data['gender'])

        # Save the full gender description in UserProfile
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.gender = full_gender
        user_profile.save()

        return user
    