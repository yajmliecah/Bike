from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView, RedirectView, CreateView
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
from django.contrib import auth

from .models import BikeUser
from bike.models import Item
from .forms import LoginForm, SignUpForm


class DashBoardView(DetailView):
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
        user = form.save(commit=False)
        messages.info(self.request, "Thanks for registering. You are now logged in.")
        user.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = auth.authenticate(email=email, password=password)
        auth.login(self.request, user)
        
        return super(SignUpView, self).form_valid(form)