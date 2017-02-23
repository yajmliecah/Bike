from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Brand, Edition, Item


class IndexView(TemplateView):
    model = Item
    template_name = ''


