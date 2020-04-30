from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class LoginForm(forms.Form):
    """
    Form allowing user login
    """
    username = forms.CharField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
