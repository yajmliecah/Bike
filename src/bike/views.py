from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Category, Brand, Edition, Item
from.forms import ItemForm

from django.core.urlresolvers import reverse, reverse_lazy


class ItemListView(ListView):
    template_name = 'bike/index.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return Item.objects.all()

    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'bike/item_detail.html'
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context
    
    
class ItemCreateView(CreateView):
    model = Item
    
    
    def get_form_class(self):
        return ItemForm
    
    
class ItemDeleteView(DeleteView):
    model = Item
    

