from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'login-field',
            'placeholder': 'E-mail'
        }))
    password = forms.CharField(label='', max_length=256, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'login-field',
            'placeholder': 'Password'
        }))
