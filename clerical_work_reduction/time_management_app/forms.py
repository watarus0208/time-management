from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ++kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    # パスワード入力・非表示対応
    password = forms.CharField(widget=forms.PasswordInput(), label='パスワード')

    