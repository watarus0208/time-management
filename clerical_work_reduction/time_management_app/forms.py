from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


User = get_user_model()


class SignupForm(UserCreationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widhet.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username',)


class MonthForm(forms.Form):
    start_time = forms.TimeField(label='start_time')
    close_time = forms.TimeField(label='close_time')
    attend_time = forms.TimeField(label='attendance_time')
    work_time = forms.TimeField(label='work_time')
    break_time = forms.TimeField(label='break_time')
    overtime_break_time = forms.TimeField(label='overtime_break_time')
    today_todo = forms.CharField(label='today_todo')
    today_issue = forms.CharField(label='today_issue')
