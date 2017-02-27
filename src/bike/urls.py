from django.conf.urls import url
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemDeleteView


urlpatterns = [
    url('^$', ItemListView.as_view(), name='item_list'),
    url(r'^item/(?P<pk>[-\w\ ]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^new/$', ItemCreateView.as_view(), name='add_item'),
    url(r'^delete/$', ItemDeleteView.as_view(), name='item_delete'),
]
