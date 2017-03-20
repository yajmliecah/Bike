from django import forms
from django.conf import settings
from django.forms.widgets import *
from django.db.models import Q
from .models import BikeUser
from bike.models import Item
from geo.models import Region, Country


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
        model = BikeUser
        fields = ['email', 'password']
        
    def clean(self):
        email = self.cleaned_data.get('email', '')
        password= self.cleaned_data.get('password', '')
        
        self.user = None
        users = BikeUser.objects.filter(Q(username=email)|Q(email=email))
        for user in users:
            if user.is_active and user.check_password(password):
                self.user = user
        if self.user is None:
            raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data
        
            
class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Username',
                'required': 'True',
            }
        )
    )
    first_name = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'First Name',
                'required': 'True',
            }
        )
    )
    last_name = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Last Name',
                'required': 'True',
            }
        )
    )
    password=forms.CharField(
        widget=PasswordInput(
            attrs={
                'placeholder': 'Password',
                'required': 'True',
            }
        )
        
    )
    password_confirm = forms.CharField(
        widget=PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'required': 'True',
            }
        )
    )
    
    email = forms.CharField(
        widget=EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'required': 'True',
            }
        )
    )
    avatar = forms.CharField(
        widget=FileInput(
            attrs={
                'placeholder': 'Picture',
            }
        )
    )
    locations = forms.ModelChoiceField(queryset=Region.objects.all(),
                                       widget=Select(
                                           attrs={
                                               'placeholder': 'Location',
                                           }
                                       )
                                       )
    
    
    class Meta:
        model = BikeUser
        fields = ['username', 'first_name', 'last_name', 'password', 'password_confirm', 'email', 'avatar']
    