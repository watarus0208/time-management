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

    def get(self, request, **kwargs):
        attendances = Attendance.objects.all() 
        
        month_data = defaultdict(dict)
        for d in range(self.month_days):
            month_data[d+1]['weekday'] = self.weekday[(d+self.first_weekday)%7]
        for a in attendances:
            month_data[a.date.day]['start_time'] = a.start_time
            month_data[a.date.day]['close_time'] = a.close_time
            month_data[a.date.day]['attend_time'] = self.get_timedelta(a.start_time, a.close_time)
            month_data[a.date.day]['work_time'] = self.get_timedelta(a.start_time, a.close_time) - self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time) 
            month_data[a.date.day]['break_time'] = self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time)
            month_data[a.date.day]['overtime_break_time'] = self.get_timedelta(a.work_pattern.start_break_time, a.work_pattern.close_break_time) 
            month_data[a.date.day]['today_todo'] = a.today_todo
            month_data[a.date.day]['today_issue'] = a.today_issue
            month_data[a.date.day]['work_pattern'] = a.work_pattern
        print(month_data)

        return render(request, 'time_management_app/month.html', month_data)


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/config.html'
