from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm

import calendar
import datetime


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
    
    def get(self, request, **kwargs):
        date = datetime.datetime.today()
        month_days = list(calendar.monthrange(date.year, date.month))
        month_days[1] = month_days[1] + 1
        params = {
            'month_days': [d for d in range(*month_days)],
        }
        return render(request, 'time_management_app/month.html', params)
    

class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/config.html'