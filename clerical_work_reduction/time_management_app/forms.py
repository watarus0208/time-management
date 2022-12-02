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
    start_time = forms.TimeField(label='開始時刻')
    close_time = forms.TimeField(label='終了時刻')
    attend_time = forms.TimeField(label='勤務時間')
    work_time = forms.TimeField(label='稼働時間')
    break_time = forms.TimeField(label='休憩時間')
    overtime_break_time = forms.TimeField(label='時間外休憩時間')
    today_todo = forms.CharField(label='予定')
    today_issue = forms.CharField(label='進捗')
