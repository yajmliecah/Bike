from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import BikeUser


class BikeUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(BikeUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        
    class Meta:
        model = BikeUser
        fields = ('email', )