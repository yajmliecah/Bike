from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import LoginView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]