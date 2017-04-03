from ..models import Item
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


class CategoryList(ListView):
    model = Item
    context_object_name = 'category'
    

class MotorcycleView(CategoryList):
    
    def get_context_data(self, **kwargs):
        context = super(MotorcycleView, self).get_context_data(**kwargs)
        
        motorcycle = Item.objects.get_motorcycles()
        
        context['motorcycle'] = motorcycle
        
        return context