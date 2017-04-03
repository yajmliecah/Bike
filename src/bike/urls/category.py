from django.conf.urls import url
from ..views import category


urlpatterns = [
    url(r'^motorcycles/$', category.MotorcycleView.as_view(), name='motorcycle'),
]
