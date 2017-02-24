from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Brand, Edition, Item


class IndexView(TemplateView):
    template_name = 'app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_bikes'] = Item.objects.all()[:10]
        return context


