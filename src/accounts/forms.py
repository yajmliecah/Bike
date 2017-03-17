from django import forms
from django.conf import settings
from django.forms.widgets import *
from .models import BikeUser

class AuthenticationForm(forms.Form):
    email = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Email',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['email', 'password']


class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = BikeUser
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'avatar', 'location']
    