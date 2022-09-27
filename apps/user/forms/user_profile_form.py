from django import forms

from apps.user.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'bio', 'avatar']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'profile-field', 'readonly': True}),
            'first_name': forms.TextInput(attrs={'class': 'profile-field'}),
            'last_name': forms.TextInput(attrs={'class': 'profile-field'}),
            'password': forms.PasswordInput(attrs={'class': 'profile-field'}),
            'bio': forms.Textarea(attrs={'class': 'profile-field', 'rows': 5}),
            'avatar': forms.FileInput(attrs={'class': 'profile-field'}),
        }
