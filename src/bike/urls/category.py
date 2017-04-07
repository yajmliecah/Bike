from django.conf.urls import url
from ..views import category


urlpatterns = [
    url(r'^car/$', category.CarListView.as_view(), name='car'),
    url(r'^motorcycle/$', category.MotorcycleListView.as_view(), name='motorcycle'),
    url(r'^vehicle/$', category.VehicleListView.as_view(), name='vehicle'),
]
