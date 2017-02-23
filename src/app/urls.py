from django.conf.urls import url
from .views import



urlpatterns = [
    url('^$', views.index, name='index'),
    
]
