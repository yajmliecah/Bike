from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url('^all/$', ItemListView.as_view(), name='items'),
    url(r'^item/(?P<slug>[-\w ]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', CategoryDetailVew.as_view(), name='categories'),
    url(r'^brand/(?P<slug>[-\w]+)/$', BrandDetailView.as_view(), name='brands'),
    url(r'^edition/(?P<slug>[-\w]+)/$', EditionDetailVew.as_view(), name='editions'),
    url(r'^search/$', ItemSearchListView.as_view(), name='search_items'),
 ]
