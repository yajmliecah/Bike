from django.conf.urls import url
from ..views import category


urlpatterns = [
    url(r'^$', category.CategoryListView.as_view(), name='categories'),
    url(r'^(?P<slug>[\w-]+)/$', category.CategoryDetailView.as_view(), name='category_detail'),
]
