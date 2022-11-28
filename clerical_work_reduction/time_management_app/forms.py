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
    start_time = forms.TimeField()
    close_time = forms.TimeField()
    attendance_time = forms.TimeField()
    work_time = forms.TimeField()
    break_time = forms.TimeField()
    overtime_break_time = forms.TimeField()
    today_plan = forms.Textarea()
    today_issue = forms.Textarea()