from django import forms
from allauth.account.forms import SignupForm, LoginForm
from django.utils.translation import gettext_lazy as _


from accounts.models import UserProfile


class CustomSignupForm(SignupForm):
    GENDER_CHOICES = [
            ('--', '--'),
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ]

    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})

    def save(self, request):
        # This will call the built-in save method which handles user creation and validation
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Mapping and saving gender to user profile
        gender_map = {'M': 'Male', 'F': 'Female', 'O': 'Other'}
        full_gender = gender_map.get(self.cleaned_data['gender'])

        # Save the full gender description in UserProfile
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.gender = full_gender
        user_profile.save()

        return user

class CustomLoginForm(LoginForm):
    login = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['remember'].widget.attrs.update({'class': 'form-check-input'})