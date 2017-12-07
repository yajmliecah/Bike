from django import forms
from django.utils.text import slugify

from .models import SubCategory, Category, Brand, Item
from geo.models import City
from django.forms.widgets import *


class ItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name' }))
    details = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Product Details'}))
    short_desc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select({'class': 'form-control'}))
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), widget=forms.Select({'class': 'form-control'}))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select({'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    stock = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    locations = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select({'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['name', 'details', 'short_desc', 'image', 'category',
                    'sub_category', 'brand', 'price', 'stock', 'locations',]
        
    def save(self, commit=True):
        
        return super(ItemForm, self).save(commit)