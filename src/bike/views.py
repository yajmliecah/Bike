from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Count, Q
from bike.models import Category, Brand, Edition, Item
from .forms import ItemForm
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


class BaseView(TemplateView):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.category = Category.objects.all()
        self.brand = Brand.get_brands()
        self.edition = Edition.get_edition()
        self.item = Item.get_items()

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['brand'] = self.brand
        context['edition'] = self.edition
        context['item'] = self.item
        if hasattr(self, 'page_title'):
            context['page_title'] = self.page_title
        return context


class IndexView(BaseView):
    template_name = 'bike/index.html'
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        return super(IndexView, self).get(request, items=items)


class ItemListView(BaseView):
    template_name = 'bike/item_list.html'
    paginate_by = 10
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        items = Item.get_items()
        paginator = Paginator(items, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return super(ItemListView, self).get(request,
                                             items=items)


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
                Q(edition__name__icontains=query) |
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
        return context


class CategoryDetailVew(BaseView):
    template_name = 'bike/category_list.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        category = Category.objects.get(slug=slug)
        items = Item.objects.all().filter(category=category)
        return super(CategoryDetailVew, self).get(request,
                                                  category=category,
                                                  items=items)


class BrandDetailView(BaseView):
    template_name = 'bike/brand_list.html'
    context_object_name = 'brands'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        brand = Brand.objects.get(slug=slug)
        items = Item.objects.filter(brand=brand)
        return super(BrandDetailView, self).get(request,
                                                brand=brand,
                                                items=items)


class EditionDetailVew(BaseView):
    template_name = 'bike/edition_list.html'
    context_object_name = 'edition'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        edition = Edition.objects.get(slug=slug)
        items = Item.objects.filter(edition=edition)
        return super(EditionDetailVew, self).get(request,
                                                 edition=edition,
                                                 items=items)
