from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse, reverse_lazy

from .models import BikeUser
from .forms import AuthenticationForm, SignUpForm

User = get_user_model()


class BikeUserListView(ListView):
    template_name = 'accounts/accountslist.html'
    context_object_name = 'bikeusers'
    queryset = BikeUser.objects.all()
    
    
class BikeUserView(DetailView):
    model = BikeUser
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super(BikeUserView, self).get_context_data(**kwargs)
        return context
    

class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = '/accounts/bikeusers/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])
        login(self.request, form.user)
  
        return super(LoginView, self).form_valid(form)
    
    
class LogoutView(RedirectView):
    
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
    

class SignUpView(FormView):
    template_name = 'accounts/signup_form.html'
    form_class = SignUpForm
    
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.save(commit=True)
        
        return super(SignUpView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    
    
    
    

    