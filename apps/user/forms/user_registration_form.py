from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.user.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'registration-field',
            'placeholder': 'E-mail'
        }))
    password1 = forms.CharField(label='', max_length=256, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'registration-field',
            'placeholder': 'Password'
        }))
    password2 = forms.CharField(label='', max_length=256, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'registration-field',
            'placeholder': 'Confirm Password'
        }))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')
