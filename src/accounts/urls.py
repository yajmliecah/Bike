from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import LoginView, LogoutView, SignUpView, BikeUserListView, BikeUserView, DashBoardView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^dashboard/(?P<pk>\d+)/$', DashBoardView.as_view(), name='dashboard'),
    url(r'^dashboard/$', DashBoardView.as_view(), name='user_detail'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^bike_users/$', BikeUserListView.as_view(), name='bike_users'),
]