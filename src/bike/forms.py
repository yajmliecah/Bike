from django import forms
from .models import Brand, Edition, Item


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'image', 'category', 'brand', 'edition', 'price',
              'condition', 'details', 'locations', 'active')
        exclude = ('slug', 'owner')