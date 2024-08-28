from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm, LoginForm
from datetime import date, datetime

from .models import *


class CustomSignupForm(SignupForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > date.today():
            raise ValidationError('Date of birth cannot be in the future.')
        return date_of_birth

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        gender_map = {'M': 'Male', 'F': 'Female', 'O': 'Other'}
        full_gender = gender_map.get(self.cleaned_data['gender'])

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.gender = full_gender
        user_profile.date_of_birth = self.cleaned_data['date_of_birth']
        user_profile.save()

        return user


class CustomLoginForm(LoginForm):
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
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['remember'].widget.attrs.update(
            {'class': 'form-check-input'}
        )


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
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

        if self.instance and self.instance.pk:
            self.fields['email'].initial = self.instance.user.email

        for field_name in self.fields:
            self.fields[field_name].required = True

        if self.instance and self.instance.pk:
            if self.instance.date_of_birth:
                self.fields['date_of_birth'].initial = (
                    self.instance.date_of_birth.strftime('%Y-%m-%d')
                )

    def clean_email(self):
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
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not phone_number.isdigit():
                raise ValidationError('Phone number must contain only digits.')
        return phone_number

    def clean_current_weight(self):
        current_weight = self.cleaned_data.get('current_weight')
        if current_weight <= 0:
            raise ValidationError('Current weight must be greater than zero.')
        return current_weight

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height <= 0:
            raise ValidationError('Height must be greater than zero.')
        return height

    def clean_goal_weight(self):
        goal_weight = self.cleaned_data.get('goal_weight')
        if goal_weight <= 0:
            raise ValidationError('Goal weight must be greater than zero.')
        return goal_weight

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')

        if date_of_birth and date_of_birth > datetime.today().date():
            self.add_error(
                'date_of_birth',
                'Date of birth cannot be in the future.'
            )

        return cleaned_data

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.email = self.cleaned_data['email']
        user.save()
        if commit:
            profile.save()
        return profile


class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight']
        widgets = {
            'weight': forms.NumberInput(
                attrs={'step': '0.1', 'class': 'form-control'}
            ),
        }


class ProgressPictureForm(forms.ModelForm):
    class Meta:
        model = ProgressPicture
        fields = ['progress_image']
