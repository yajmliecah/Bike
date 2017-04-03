import operator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..models import Brand, Edition, Item
from ..forms import ItemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from ..search import *
        

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
        results = Item.objects.all()
        paginator = Paginator(results, self.paginate_by)
        
        page = self.request.GET.get('page')
        
        query = self.request.GET.get('q')
        
        if query is not None:
            results = Item.objects.filter(
                Q(name__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {
            'items': items,
            'results': results
        }
        return context
    

class CarView(ItemListView):
    template_name = 'bike/car_list.html'
    context_object_name = 'cars'
    
    def get_context_data(self, **kwargs):
        context = super(CarView, self).get_context_data(**kwargs)

        car = Item.objects.get_car()
        
        context['car'] = car
        return context


class MotorcycleView(ItemListView):
    template_name = 'bike/motorcycle_list.html'
    context_object_name = 'motorcycle'
    
    def get_context_data(self, **kwargs):
        context = super(MotorcycleView, self).get_context_data(**kwargs)
        motorcycle = Item.objects.get_motorcycle()
        
        context['motorcycle'] = motorcycle
        
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

        

