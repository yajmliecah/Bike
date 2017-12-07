from django.views.generic import ListView, DetailView, FormView, RedirectView, CreateView
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib import auth
from .models import BikeUser
from bike.models import SubCategory, Category, Brand, Item
from .forms import LoginForm, SignUpForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = '/products/product_list/'
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


def create_account(request):

    form = SignUpForm(request.POST or None)

    if request.POST and form.is_valid():
        form.save()
        messages.info(request, "You're signed up! Use the login form below to get started.")
        return HttpResponseRedirect(reverse('login'))

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))


    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


'''
class DashBoardView(DetailView):
    template_name = 'accounts/dashboard.html'

    def get_object(self):
        user = self.request.user
        return user

    def get_context_data(self, **kwargs):
        context = super(DashBoardView, self).get_context_data(**kwargs)
        items = []
        if self.request.user.is_authenticated():
            items = Item.objects.filter(owner=self.request.user)
        else:
            items = []

        context['items'] = items
        return context
'''

""""
class SignUpView(FormView):
    model = BikeUser
    template_name = 'accounts/signup_form.html'
    form_class = SignUpForm
    success_url = '/accounts/dashboard/'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        user = BikeUser.objects.create(
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password1']
        )
        return super(SignUpView, self).form_valid(form)

"""
