from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ++kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

User = get_user_model()

class SignupForm(UserCreationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ('username',)