from django import forms
from django.contrib.auth.models import User


class LoginViewForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full'
        })
    )


class RegisterViewForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input input-bordered w-full'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input input-bordered w-full'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input input-bordered w-full'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )

    def clean(self):
        cleaned = super().clean()

        if cleaned.get("password") != cleaned.get("password2"):
            raise forms.ValidationError("Passwords don't match")

        if User.objects.filter(username=cleaned.get("username")).exists():
            raise forms.ValidationError("User with this username already exists.")

        return cleaned


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
    new_password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full'})
    )
