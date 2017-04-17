from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from ..models import Brand, Edition, Item
from ..forms import ItemForm
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..search import *
        

class BaseView(ListView):
    
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        
        self.brand = Brand.get_brand()
        self.edition = Edition.get_edition()
        self.item = Item.get_items()
        
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        
        breadcrumbs = ({'name': 'Home', 'url': '/'},)
        
        if 'breadcrumbs' in context:
            breadcrumbs += context['breadcrumbs']
        
        context['breadcrumbs'] = breadcrumbs
        context['brand'] = self.brand
        context['edition'] = self.edition
        context['item'] = self.item
        
        return context


class ItemListView(BaseView):
    model = Item
    template_name = 'bike/item_list.html'
    paginate_by = 10
    
    def __init__(self, *args, **kwargs):
        super(ItemListView, self).__init__(*args, **kwargs)
        
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        all_item = Item.get_items()
        paginator = Paginator(all_item, self.paginate_by)
        page = self.request.GET.get('page')
        
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
            
        context['all_item'] = items
        context['item'] = Item.objects.order_by('-submitted_on')
        return context


class ItemSearchListView(ItemListView):
    template_name = 'bike/search.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ItemSearchListView, self).get_context_data(**kwargs)
        results = Item.objects.all()
        
        query = self.request.GET.get('q')
        
        if query is not None:
            results = Item.objects.filter(
                Q(name__icontains=query) |
                Q(category__icontains=query)
            ).distinct()
        
        context['results'] = results
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ItemCreateView, self).dispatch(*args, **kwargs)
    
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