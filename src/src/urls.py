from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('bike.urls.items', namespace='items')),
    url(r'^category/', include('bike.urls.category', namespace='category')),
    url(r'^admin/', admin.site.urls),
]
