from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('bike.urls', namespace='Bike')),
    url(r'^admin/', admin.site.urls),
]
