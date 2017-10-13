from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Count, Q
from .models import SubCategory, Category, Brand, Item
from .forms import ItemForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from .utils import paginate


class BaseView(TemplateView):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.categories = Category.top_categories()
        self.brands = Brand.get_brands()
        self.item = Item.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        context['brands'] = self.brands
        context['item'] = self.item
        
        if hasattr(self, 'page_title'):
            context['page_title'] = self.page_title
        return context


class IndexView(BaseView):
    template_name = 'index.html'
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(active=True)[:8]
        brands = Brand.top_brands()[:8]
        return super(IndexView, self).get(request, items=items, brands=brands)
    

class CategoryDetailVew(BaseView):
    template_name = 'bike/category_items.html'
    
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        category = next((category for category in self.categories if category.slug == slug), None)
        items = paginate(request, Item.category_items(category))
        return super(CategoryDetailVew, self).get(request,
                                                  category=category,
                                                  items=items,
                                                  )
    

class BrandDetailView(BaseView):
    template_name = 'bike/brand_items.html'
   
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        brand = next((brand for brand in self.brands if brand.slug == slug), None)
        items = paginate(request, Item.brand_items(brand))
        return super(BrandDetailView, self).get(request,
                                                brand=brand,
                                                items=items
                                                )
    
    
class ItemListView(BaseView):
    template_name = 'bike/all_items.html'
    
    def get(self, request, *args, **kwargs):
        items = paginate(request, Item.objects.filter(active=True). order_by("-submitted_on"))
        return super(ItemListView, self).get(request,
                                             items=items)


class ItemSearchListView(ItemListView):
    template_name = 'bike/search.html'
    
    def get_context_data(self, **kwargs):
        context = super(ItemSearchListView, self).get_context_data(**kwargs)
        results = Item.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            results = Item.objects.filter(
                Q(name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(locations__name__icontains=query)
            ).distinct()
        context['results'] = results
        context['query'] = query
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'bike/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.get_categories()
        context['brand'] = Brand.get_brands()
        return context