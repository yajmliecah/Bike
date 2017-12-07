from django.conf.urls import url
from ..views import add_items


urlpatterns = [
    url('^product_list/$', add_items.product_list, name='product_list'),
    url('^add_product/$', add_items.add_product, name='add_product'),
    url('^update_product/(?P<slug>[\w-]+)/$', add_items.update_product, name='update_product'),
    url('^delete/(?P<slug>[\w-]+)/$', add_items.delete_product, name='delete_product')
]
