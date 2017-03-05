from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..models import Brand, Edition, Item
from ..forms import ItemForm
from django.contrib import messages

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


class ItemListView(ListView):
    model = Item
    template_name = 'bike/index.html'
    context_object_name = 'items'
    q = ""
    
    def get_queryset(self):
        try:
            name = self.kwargs['name']
        except:
            name = ''
            
            if (name != ''):
                items =self.model.objects.filter(name__icontains=name)
            else:
                items = self.model.objects.all()
        
        return items
           
    def get(self, request, *args, **kwargs):
        qs = Item.objects.all()
        q = request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(category__icontains=q)
            ).distinct()
        else:
            q = Item.objects.all()
                
        return super(ItemListView, self).get(request, *args, **kwargs)
    
    
    
    
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
    
        

