from django.conf.urls import url
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemDeleteView, ItemUpdateView


urlpatterns = [
    url('^$', ItemListView.as_view(), name='item_list'),
    url(r'^new/$', ItemCreateView.as_view(), name='add_item'),
    url(r'^edit/(?P<pk>[-\w ]+)/$', ItemUpdateView.as_view(), name='edit_item'),
    url(r'^item/(?P<pk>[-\w ]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^delete/(?P<pk>[-\w ]+)/$', ItemDeleteView.as_view(), name='item_delete'),
    
]
