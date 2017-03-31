from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView, RedirectView, TemplateView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseForbidden
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib import messages

from .models import BikeUser
from bike.models import Item
from .forms import LoginForm, SignUpForm


class BikeUserListView(ListView):
    model = BikeUser
    template_name = 'accounts/accountslist.html'
    context_object_name = 'bike_users'
    
    def get_queryset(self):
        bike_users = BikeUser.objects.all()
        return bike_users

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BikeUserListView, self).dispatch(*args, **kwargs)
    
    
class BikeUserView(DetailView):
    model = BikeUser
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'bike_user'
    

class DashBoardView(BikeUserView):
    template_name = 'accounts/dashboard.html'
    
    def get_object(self):
        return self.request.user
        
    def get_context_data(self, **kwargs):
        context = super(DashBoardView, self).get_context_data(**kwargs)
        items = []
        if self.request.user.is_authenticated():
            items = Item.objects.filter(owner=self.request.user)
        else:
            items = []
        
        context['items'] = items
        return context
        

class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = '/accounts/dashboard/'
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])
        login(self.request, form.user)
    
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
    
        return super(LoginView, self).form_valid(form)
    
    
class LogoutView(RedirectView):
    
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
    

class SignUpView(FormView):
    template_name = 'accounts/signup_form.html'
    form_class = SignUpForm
    success_url = '/accounts/dashboard/'
    
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Thanks for registering. You are now logged in.")
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, form.user)
        
        return super(SignUpView, self).form_valid(form)
   
    
    
    
    