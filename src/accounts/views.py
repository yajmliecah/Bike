from django.shortcuts import render, render_to_response
from django.views.generic import FormView
from .models import Profile
from .forms import ProfileForm, UserForm


class SignUpView(FormView):
    form_class = ProfileForm
    template_name = 'accounts/signup_form.html'
    success_url = 'accounts/profile_detail'
        
    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        user_form.prefix = 'user_form'
        profile_form = ProfileForm()
        profile_form.prefix = 'profile_form'
        return self.render_to_response(self.get_context_data('user_form', user_form, 'profile_form', profile_form))
    
    def post(self, request, *args, **kwargs):
        user_form = UserForm(self.request.POST, prefix='user_form')
        profile_form = ProfileForm(self.request.POST, prefix='profile_form')
        
                
                    
    def get_initial(self):
        initial = super(SignUpView, self).get_initial()
        initial['request'] = self.request
            
        return initial
   
    def form_valid(self, form):
        form.save(commit=True)
        return super(SignUpView, self).form_valid(form)