from django.conf.urls import url
from .views import SignUpView


urlpatterns = [
    url(r'^sign_up/$', SignUpView.as_view(), name='signup'),
]
