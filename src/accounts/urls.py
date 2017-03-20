from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import LoginView, LogoutView, SignUpView, BikeUserView, BikeUserListView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^profile/(?P<pk>[-\w ]+)/$', BikeUserView.as_view(), name='profile'),
    url(r'^bikeusers/$', BikeUserListView.as_view(), name='bikeusers'),
]