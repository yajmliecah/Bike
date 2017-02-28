from django.conf.urls import url
from ..views import category


urlpatterns = [
    url(r'^cars/$', category.cars, name='cars'),
    url(r'^motors/$', category.motors, name='motors'),
    url(r'^vehicles/$', category.vehicles, name='vehicles'),
    
    
]
