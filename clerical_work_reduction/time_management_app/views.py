from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from . import forms


class LoginView(LoginView):
    form_class: forms.LoginForm
    template_name = 'time_management_app/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'time_management_app/login.html'


class SignUpView(CreateView):
    form_class = forms.SignupForm
    template_name = 'time_management_app/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        return redirect('time_management_app:login')        

