from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Brand, Edition, Item
from.forms import ItemForm

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


class ItemListView(ListView):
    template_name = 'bike/index.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return Item.objects.all()

    
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
        form.instance.user = self.request.user
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

