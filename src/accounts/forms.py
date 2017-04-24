from django import forms
from django.conf import settings
from django.forms.widgets import *
from django.db.models import Q
from .models import BikeUser
from bike.models import Item
from geo.models import City, Country
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Email',
                'required': 'True',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                'placeholder': 'Password',
                'required': 'True',
                'class': 'form-control',
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
        
            
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Username',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'First Name',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Last Name',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    password1=forms.CharField(
        label="Password",
        widget=PasswordInput(
            attrs={
                'placeholder': 'Password',
                'required': 'True',
                'class': 'form-control'
            }
        )
        
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    
    email = forms.CharField(
        widget=EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'required': 'True',
                'class': 'form-control'
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
    locations = forms.ModelChoiceField(queryset=City.objects.all(),
                                       widget=Select(
                                           attrs={
                                               'placeholder': 'Location',
                                               'class': 'form-control'
                                           }
                                       )
                                       )
    
    
    class Meta:
        model = BikeUser
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):
        username = self.cleaned_data.get('username', '')
        email = self.cleaned_data.get('email', '')
        password = self.cleaned_data.get('password', '')
        
    
        self.user = None
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user