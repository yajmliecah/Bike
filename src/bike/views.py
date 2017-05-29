from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Q
from .models import Category, Brand, Edition, Item
from .forms import ItemForm
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BaseView(ListView):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.category = Category.get_category()
        self.brand = Brand.get_brand()
        self.edition = Edition.get_edition()
        self.item = Item.get_items()
    
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        
        breadcrumbs = ({'name': 'Home', 'url': '/'},)
        
        if 'breadcrumbs' in context:
            breadcrumbs += context['breadcrumbs']
        
        context['breadcrumbs'] = breadcrumbs
        context['category'] = self.category
        context['brand'] = self.brand
        context['edition'] = self.edition
        context['item'] = self.item
        
        return context


class IndexView(TemplateView):
    template_name = 'bike/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        top_brands = Brand.objects.top_brands()[:3]
        featured_cars = Item.featured_car()
        
        context['top_brands'] = top_brands
        context['featured_cars'] = featured_cars
        
        return context


class ItemListView(BaseView):
    model = Item
    template_name = 'bike/item_list.html'
    paginate_by = 10
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        items = Item.objects.all()
        paginator = Paginator(items, self.paginate_by)
        page = self.request.GET.get('page')
        
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        
        context['items'] = items
        
        return context


class ItemSearchListView(ItemListView):
    template_name = 'bike/search.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ItemSearchListView, self).get_context_data(**kwargs)
        results = Item.get_items()
        
        query = self.request.GET.get('q')
        
        if query is not None:
            results = Item.objects.filter(
                Q(name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(edition__name__icontains=query) |
                Q(locations__name__icontains=query)
            ).distinct()
        
        context['results'] = results
        context['query'] = query
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'bike/item_detail.html'
    context_object_name = 'items'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('dashboard')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ItemCreateView, self).dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = super(ItemCreateView, self).get_initial()
        initial['request'] = self.request
        return initial
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        messages.success(self.request, 'File Uploaded')
        self.object.owner = self.request.user
        self.object.save()
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    success_url = reverse_lazy('dashboard')
    form_class = ItemForm
    template_name_suffix = '_update_form'


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('dashboard')


class CategoryDetailVew(DetailView):
    model = Category
    template_name = 'bike/category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailVew, self).get_context_data(**kwargs)
        obj = self.get_object()
        item_set = obj.item_set.all()
        items = (item_set).distinct()
        category = Category.get_category()
        context['category'] = category
        context['items'] = items
        
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'bike/brand_detail.html'
    context_object_name = 'brand'
    
    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        
        item_set = obj.item_set.all()
        items = (item_set).distinct()
        
        context['items'] = items
        
        return context


class EditionDetailVew(DetailView):
    model = Edition
    template_name = 'bike/edition_detail.html'
    context_object_name = 'edition'
    
    def get_context_data(self, **kwargs):
        context = super(EditionDetailVew, self).get_context_data(**kwargs)
        obj = self.get_object()
        item_set = obj.item_set.all()
        items = (item_set).distinct()
        
        context['items'] = items
        
        return context



