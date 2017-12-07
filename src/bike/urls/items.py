from django.conf.urls import url
from ..views import items


urlpatterns = [
    url('^$', items.IndexView.as_view(), name='index'),
    url('^all/$', items.ItemListView.as_view(), name='items'),
    url('^sub_category/(?P<slug>[\w-]+)/$', items.SubCategoryDetail.as_view(), name='sub_categories'),
    url(r'^category/(?P<slug>[\w-]+)/$', items.CategoryDetailVew.as_view(), name='categories'),
    url(r'^brand/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', items.BrandDetailView.as_view(), name='brands'),
    url(r'^item/(?P<slug>[-\w ]+)/$', items.ItemDetailView.as_view(), name='item_detail'),
    url(r'^search/$', items.ItemSearchListView.as_view(), name='search_items'),
 ]
