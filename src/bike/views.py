from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Brand, Edition, Item


class IndexView(ListView):
    template_name = 'bike/index.html'
    context_object_name = 'all_items'
    
    def get_queryset(self):
        return Item.objects.all()


class DetailView(DetailView):
    model = Item
    template_name = 'bike/details.html'
    
    


