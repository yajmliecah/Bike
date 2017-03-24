from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.list import BaseListView
from django.db.models import Q
from ..models import Brand, Edition, Item
from ..forms import ItemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
        

class FeaturedView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'bike/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(FeaturedView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.all()[:8]
        return context
    

class ItemListView(ListView):
    model = Item
    context_object_name = 'item'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        items = Item.objects.all()
        queryset_list = Item.objects.none()
        paginator = Paginator(items, self.paginate_by)

        query = self.request.GET.get('q', '')
        if query:
            queryset_list = Item.objects.filter(
                Q(name__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
        
        
        page = self.request.GET.get('page')
        
        try:
            item_list = paginator.page(page)
        except PageNotAnInteger:
            item_list = paginator.page(1)
        except EmptyPage:
            item_list = paginator.page(paginator.num_pages)
        
        context['items'] = item_list
        context['query'] = query
        context['querset_list'] = queryset_list
        return context
        
    
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
        bike = form.save(commit=False)
        messages.success(self.request, 'File Uploaded')
        bike.owner = self.request.user
        bike.save()
        
        return super(ItemCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('items:index')
    

class ItemUpdateView(UpdateView):
    model = Item
    success_url = reverse_lazy('items:item_list')
    form_class = ItemForm
    template_name_suffix = '_update_form'
    
    
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:item_list')
    
        

