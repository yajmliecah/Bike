from django.conf.urls import url
from ..views import items


urlpatterns = [
    url('^$', items.ItemListView.as_view(), name='all_items'),
    url(r'^new/$', items.ItemCreateView.as_view(), name='add_item'),
    url(r'^edit/(?P<pk>[-\w ]+)/$', items.ItemUpdateView.as_view(), name='edit_item'),
    url(r'^item/(?P<slug>[-\w]+)/$', items.ItemDetailView.as_view(), name='item_detail'),
    url(r'^delete/(?P<pk>[-\w ]+)/$', items.ItemDeleteView.as_view(), name='item_delete'),
    url(r'^search/$', items.ItemSearchListView.as_view(), name='search_items'),
 ]

