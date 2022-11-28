from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'time_management_app/login.html'
     

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'time_management_app/login.html'


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'time_management_app/signup.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('time_management_app:login')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/home.html'


class MonthView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/month.html'


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/config.html'