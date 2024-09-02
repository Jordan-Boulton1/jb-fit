import re
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm, LoginForm
from datetime import date, datetime

from .models import *


# Custom signup form extending from allauth's SignupForm
class CustomSignupForm(SignupForm):
    # Define choices for gender
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Define additional fields for the signup form
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        required=True
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        required=True
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label='Gender',
        required=True,
        widget=forms.RadioSelect
    )
    date_of_birth = forms.DateField(
        label='Date of Birth',
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    # Define password fields with customized widgets
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        # Initialize the form and customize field widgets
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # Remove the colon suffix from labels
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['gender'].widget.attrs.update(
            {'class': 'form-check-input'}
        )
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control'}
        )

    def clean_first_name(self):
        # Validate that the first name contains only letters
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[a-zA-Z]+$', first_name):
            raise ValidationError(
                'First name can only contain alphabetical characters.'
            )
        return first_name

    def clean_last_name(self):
        # Validate that the last name contains only letters
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[a-zA-Z]+$', last_name):
            raise ValidationError(
                'Last name can only contain alphabetical characters.'
            )
        return last_name

    def clean_date_of_birth(self):
        # Validate that the date of birth is not in the future
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > date.today():
            raise ValidationError('Date of birth cannot be in the future.')
        return date_of_birth

    def save(self, request):
        # Save the user and associated profile data
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Map gender short codes to full descriptions
        gender_map = {'M': 'Male', 'F': 'Female', 'O': 'Other'}
        full_gender = gender_map.get(self.cleaned_data['gender'])

        # Create or update the user profile with gender and date of birth
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.gender = full_gender
        user_profile.date_of_birth = self.cleaned_data['date_of_birth']
        user_profile.save()

        return user


# Custom login form extending from allauth's LoginForm
class CustomLoginForm(LoginForm):
    # Override login and password fields to use custom widgets
    login = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        # Initialize the form and customize field widgets
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['remember'].widget.attrs.update(
            {'class': 'form-check-input'}
        )

    def clean_login(self):
        # Get the email value from the form
        email = self.cleaned_data.get('login')

        # Check if the email is in a valid format
        if email:
            try:
                # EmailField's built-in validation is used here
                forms.EmailField().clean(email)
            except ValidationError:
                # Raise a validation error if the email is not valid
                raise ValidationError(_("Enter a valid email address."))

        return email


# Form for editing the user's profile
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'phone_number',
            'address',
            'date_of_birth',
            'current_weight',
            'height',
            'goal_weight',
            'image'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'current_weight': forms.NumberInput(attrs={'step': '0.1'}),
            'height': forms.NumberInput(attrs={'step': '0.1'}),
            'goal_weight': forms.NumberInput(attrs={'step': '0.1'}),
        }

        labels = {
            'date_of_birth': 'Date of Birth',
        }

    def __init__(self, *args, **kwargs):
        # Initialize the form and customize field widgets
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

        # Set the initial value of the email field to the user's email
        if self.instance and self.instance.pk:
            self.fields['email'].initial = self.instance.user.email

        # Set all fields as required
        for field_name in self.fields:
            self.fields[field_name].required = True

        # Set the initial date format for date_of_birth if it exists
        if self.instance and self.instance.pk:
            if self.instance.date_of_birth:
                self.fields['date_of_birth'].initial = (
                    self.instance.date_of_birth.strftime('%Y-%m-%d')
                )

    def clean_email(self):
        # Validate that the email is not already in use by another user
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required.')

        if self.instance and self.instance.pk:
            original_email = self.instance.user.email
            if email != original_email:
                if User.objects.filter(
                        email=email).exclude(
                            pk=self.instance.user.pk).exists():
                    raise ValidationError(
                        'This email address is already in use.'
                    )
        else:
            if User.objects.filter(email=email).exists():
                raise ValidationError('This email address is already in use.')

        return email

    def clean_phone_number(self):
        # Validate that the phone number contains only digits
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not phone_number.isdigit():
                raise ValidationError('Phone number must contain only digits.')
        return phone_number

    def clean_current_weight(self):
        # Validate that the current weight is a positive number
        current_weight = self.cleaned_data.get('current_weight')
        if current_weight <= 0:
            raise ValidationError('Current weight must be greater than zero.')
        return current_weight

    def clean_height(self):
        # Validate that the height is a positive number
        height = self.cleaned_data.get('height')
        if height <= 0:
            raise ValidationError('Height must be greater than zero.')
        return height

    def clean_goal_weight(self):
        # Validate that the goal weight is a positive number
        goal_weight = self.cleaned_data.get('goal_weight')
        if goal_weight <= 0:
            raise ValidationError('Goal weight must be greater than zero.')
        return goal_weight

    def clean(self):
        # Perform overall form validation, including cross-field validation
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')

        # Check if date_of_birth is in the future
        if date_of_birth and date_of_birth > datetime.today().date():
            self.add_error(
                'date_of_birth',
                'Date of birth cannot be in the future.'
            )

        return cleaned_data

    def save(self, commit=True):
        # Save the profile and update the user's email
        profile = super().save(commit=False)
        user = profile.user
        user.email = self.cleaned_data['email']
        user.save()
        if commit:
            profile.save()
        return profile


# Form for logging weight entries
class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight']
        widgets = {
            'weight': forms.NumberInput(
                attrs={'step': '0.1', 'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        # Initialize the form and set label suffix to empty
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    # Clean method for the weight field
    def clean_weight(self):
        # Validate that the weight is a positive number
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise ValidationError('Value must be greater than zero.')
        return weight


# Form for uploading progress pictures
class ProgressPictureForm(forms.ModelForm):
    class Meta:
        model = ProgressPicture
        fields = ['progress_image']
