from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import LoginView, SignUpView, BikeUserView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^profile/(?P<pk>[-\w ]+)/$', BikeUserView.as_view(), name='profile'),
]