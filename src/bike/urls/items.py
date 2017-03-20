from django.conf.urls import url
from ..views import items


urlpatterns = [
    url('^$', items.IndexView.as_view(), name='index'),
    url(r'^new/$', items.ItemCreateView.as_view(), name='add_item'),
    url(r'^edit/(?P<pk>[-\w ]+)/$', items.ItemUpdateView.as_view(), name='edit_item'),
    url(r'^item/(?P<pk>[-\w ]+)/$', items.ItemDetailView.as_view(), name='item_detail'),
    url(r'^delete/(?P<pk>[-\w ]+)/$', items.ItemDeleteView.as_view(), name='item_delete'),

]

