from django.conf.urls import url
from ..views import items


urlpatterns = [
    url('^$', items.FeaturedView.as_view(), name='index'),
    url('^all/$', items.ItemListView.as_view(), name='all_items'),
    url(r'^new/$', items.ItemCreateView.as_view(), name='add_item'),
    url(r'^edit/(?P<pk>[-\w ]+)/$', items.ItemUpdateView.as_view(), name='edit_item'),
    url(r'^item/(?P<pk>[-\w ]+)/$', items.ItemDetailView.as_view(), name='item_detail'),
    url(r'^delete/(?P<pk>[-\w ]+)/$', items.ItemDeleteView.as_view(), name='item_delete'),
    url(r'^car/$', items.CarView.as_view(), name='car'),
    url(r'^motorcycle/$', items.MotorcycleView.as_view(), name='motorcycle'),
 ]

