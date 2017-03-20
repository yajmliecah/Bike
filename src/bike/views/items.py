from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.list import BaseListView
from django.db.models import Q
from ..models import Brand, Edition, Item
from ..forms import ItemForm
from django.contrib import messages

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
        

class IndexView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'bike/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['featured_items'] = Item.objects.featured_items()[:8]
        return context
    

class ItemListView(ListView):
    model = Item
    context_object_name = 'item'
    
    def get_queryset(self):
       
       return Item.objects.order_by('-submitted_on')[:8]
           
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'bike/item_detail.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context
    
    
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    
    def get_initial(self):
        initial = super(ItemCreateView, self).get_initial()
        initial['request'] =  self.request
        return initial
        
    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'File Uploaded')
        return super(ItemCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('items:item_list')
    

class ItemUpdateView(UpdateView):
    model = Item
    success_url = reverse_lazy('items:item_list')
    form_class = ItemForm
    template_name_suffix = '_update_form'
    
    
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:item_list')
    
        

