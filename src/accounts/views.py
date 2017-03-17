from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy

from .models import BikeUser
from .forms import AuthenticationForm, SignUpForm


User = get_user_model()


class BikeUserListView(ListView):
    template_name = 'acounts/acountslist.html'
    context_object_name = 'accounts'
    queryset =BikeUser.objects.all()
    
    
class BikeUserView(DetailView):
    model = BikeUser
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super(BikeUserView, self).get_context_data(**kwargs)
        return context
    

class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = '/accounts/profile/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()
    
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])
        login(self.request, user)
    
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
    
        return super(LoginView, self).form_valid(form)
    

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
    
    
    
    
    

    