from django.conf.urls import url
from ..views import brand


urlpatterns = [
    url(r'^$', brand.BrandListView.as_view(), name='brands'),
    url(r'^(?P<slug>[\w-]+)/$', brand.BrandDetailView.as_view(), name='brand_detail'),
]
