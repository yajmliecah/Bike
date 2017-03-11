from .models import Profile
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields =('username', 'email', 'password',)


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('user', 'location', 'avatar', 'mobile_number')
        exclude = ('membership', )
        
    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)

        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)