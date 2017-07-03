from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^$', IndexView.as_view(), name='all_items'),
    url('^all/$', ItemListView.as_view(), name='all_items'),
    url(r'^new/$', ItemCreateView.as_view(), name='add_item'),
    url(r'^edit/(?P<pk>[-\w ]+)/$', ItemUpdateView.as_view(), name='edit_item'),
    url(r'^item/(?P<slug>[-\w ]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^category/(?P<slug>[-\w ]+)/$', CategoryDetailVew.as_view(), name='category_detail'),
    url(r'^brand/(?P<slug>[-\w]+)/$', BrandDetailView.as_view(), name='brand_detail'),
    url(r'^edition/(?P<slug>[-\w]+)/$', EditionDetailVew.as_view(), name='edition_detail'),
    url(r'^delete/(?P<pk>[-\w ]+)/$', ItemDeleteView.as_view(), name='item_delete'),
    url(r'^search/$', ItemSearchListView.as_view(), name='search_items'),
 ]

