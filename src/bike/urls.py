from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url('^all/$', ItemListView.as_view(), name='items'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryDetailVew.as_view(), name='categories'),
    url(r'^brand/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', BrandDetailView.as_view(), name='brands'),
    url(r'^item/(?P<slug>[-\w ]+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^search/$', ItemSearchListView.as_view(), name='search_items'),
 ]
