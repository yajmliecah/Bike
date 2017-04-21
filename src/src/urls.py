from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('bike.urls.items', namespace='items')),
    url(r'^category/', include('bike.urls.category', namespace='category')),
    url(r'^brand/', include('bike.urls.brand', namespace='brand')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
