from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm
from .models import Attendance

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
        return redirect('time_management_app:home')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/home.html'


class MonthView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/month.html'

    def get(self, request, **kwargs):
        week_name = ['月', '火', '水', '木', '金', '土', '日']
        table_rows = []
        table_data = {}
        date = datetime.datetime.today()
        month_days = calendar.monthrange(date.year, date.month)[1]
        first_day = calendar.weekday(date.year, date.month, 1)
        for d in range(month_days):
            table_rows.append(
                {'day': d+1, 'weekday': week_name[(d+first_day) % 7]})
        table_data['table_data'] = table_rows
        
        data = Attendance.objects.all()
        print(data)
        return render(request, 'time_management_app/month.html', table_data)


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'time_management_app/config.html'
