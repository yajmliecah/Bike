from django.conf.urls import url
from ..views import category


urlpatterns = [
    url(r'^car/$', category.CarListView.as_view(), name='car'),
]
