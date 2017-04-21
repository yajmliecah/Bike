from django.views.generic import ListView, DetailView
from ..models import Category, Item, Brand, Edition
from django.shortcuts import render, get_object_or_404, redirect


class CategoryBaseView(ListView):
    def __init__(self, *args, **kwargs):
        super(CategoryBaseView, self).__init__(*args, **kwargs)
        self.category = Category.get_category()
     
    def get_context_data(self, **kwargs):
        context = super(CategoryBaseView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CategoryListView(CategoryBaseView):
    model = Category
    template_name = 'bike/category/category_list.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'bike/category/category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        item_set = obj.item_set.all()
        items = (item_set).distinct()
        category = Category.get_category()
        brand = Brand.get_brand()
        context['brand'] = brand
        context['category'] = category
        context['items'] = items
        
        return context
    
    