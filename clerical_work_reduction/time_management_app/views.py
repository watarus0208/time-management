from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm
from .models import Attendance
from . import mixins

import calendar
import datetime
from collections import defaultdict
import pprint


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
        return redirect('time_management_app:home')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/home.html'


class MonthView(mixins.MonthCalendarMixin, LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_calendar_data()
        context.update(calendar_context)
        pprint.pprint(context)
        return context


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/config.html'
