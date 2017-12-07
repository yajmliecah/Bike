from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from ..models import SubCategory, Category, Brand, Item
from ..forms import ItemForm
from ..utils import paginate


class BaseView(TemplateView):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.sub_categories = SubCategory.objects.all()
        self.categories = Category.objects.all()
        self.brands = Brand.get_brands()
        self.item = Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['sub_categories'] = self.sub_categories
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
        items = Item.objects.filter(active=True)
        brands = Brand.top_brands()
        return super(IndexView, self).get(request, items=items, brands=brands)


class SubCategoryDetail(BaseView):
    template_name = 'bike/category_items.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        sub_categories = next((sub_category for sub_category in self.sub_categories if sub_category.slug == slug), None)
        items = paginate(request, Item.sub_category_items(sub_categories))
        return super(SubCategoryDetail, self).get(request,
                                                  sub_categories=sub_categories,
                                                  items=items
                                                  )


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
                Q(sku__icontains=query) |
                Q(category__name__icontains=query) |
                Q(brand__name__icontains=query) |
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
        context['items'] = Item.objects.all()
        return context
