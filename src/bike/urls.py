from django.conf.urls import url
from .views import IndexView, ItemDetailView, ItemCreateView, ItemDeleteView


urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^new/$', ItemCreateView.as_view(), name='add_item'),
    url(r'^item/(?P<item_id>[0-9]+)/delete_item/(?P<pk>[0-9]+)/$', ItemDeleteView.as_view(), name='delete_item'),
]
