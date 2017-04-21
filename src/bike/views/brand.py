from django.views.generic import ListView, DetailView
from ..models import Category, Item, Brand, Edition


class BrandListView(ListView):
    model = Brand
    template_name = 'bike/brand/brand_list.html'
    context_object_name = 'brands'
    
    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'bike/brand/brand_detail.html'
    context_object_name = 'brand'
    
    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        item_set = obj.item_set.all()
        items = (item_set).distinct()
        category = Category.get_category()
        brand = Brand.get_brand()
        context['brand'] = brand
        context['category'] = category
        context['items'] = items
        
        return context