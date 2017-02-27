from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('bike.urls', namespace='items')),
    url(r'^admin/', admin.site.urls),
]
