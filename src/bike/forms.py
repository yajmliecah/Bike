from django import forms
from .models import Category, Brand, Edition, Item
from django.forms.widgets import *


class ItemForm(forms.ModelForm):
    name = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Name',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    image = forms.CharField(
        widget=FileInput(
            attrs={
                'placeholder': 'Picture',
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=Select(
            attrs={
                'placeholder': 'Category',
                'class': 'form-control'
            }
        )
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=Select(
            attrs={
                'placeholder': 'Brand',
                'class': 'form-control'
            }
        )
    )
    edition = forms.ModelChoiceField(
        queryset=Edition.objects.all(),
        widget=Select(
            attrs={
                'placeholder': 'Edition',
                'class': 'form-control'
            }
        )
    )
    price = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Price',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    company = forms.CharField(
        widget=TextInput(
            attrs={
                'placeholder': 'Company',
                'required': 'True',
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Item
        fields = ['name', 'image', 'category', 'brand', 'edition', 'price',
              'condition', 'details', 'locations']