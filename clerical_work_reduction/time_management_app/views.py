from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms


class LoginView(LoginView):
    form_class: forms.LoginForm
    template_name = 'time_management_app/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'time_management_app/login.html'


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'time_management_app/signup.html'
    success_url = reverse_lazy('time_management_app:login')
