from django import forms
from apps.users.models import User


class PasswordValidationForm(forms.Form):
    password1 = forms.CharField(label='Password', 
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', 
        widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            msg = "Passwords mismatch"
            raise forms.ValidationError('Password mismatch')
        return password2


class UserCreationForm(PasswordValidationForm):
    # create user
    email = forms.CharField(required=True, max_length=128,
        label='Email Address')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError('User with this email already exists')
        except User.DoesNotExist:
            return email


class CompanyCreationForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=128, label='Company Name')
