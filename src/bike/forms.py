from django import forms
from .models import Brand, Category, Edition, Item


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'category', 'brand', 'edition', 'price', 'negotiable',
              'condition', 'seller_type', 'fuel', 'transmission', 'lifestyle', 'color_family', 'details')
        exclude = ('slug',)

       

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)