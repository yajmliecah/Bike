from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .models import BikeUser
from .forms import AuthenticationForm


User = get_user_model()


class BikeUserListView(ListView):
    template_name = 'acounts/acountslist.html'
    context_object_name = 'accounts'
    queryset =BikeUser.objects.all()


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
    
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
    
        return super(LoginView, self).form_valid(form)

    
    
    

    