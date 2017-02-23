from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('Car.urls', namespace='Car')),
    url(r'^admin/', admin.site.urls),
]
