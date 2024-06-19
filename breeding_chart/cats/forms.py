from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cat, Tomcat


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['cats_name', 'breeder_name', 'color', 'mothers_name', 'fathers_name', 'birth_date', 'photo']


class TomcatForm(forms.ModelForm):
    class Meta:
        model = Tomcat
        fields = ['cats_name', 'breeder_name', 'color', 'mothers_name', 'fathers_name', 'birth_date', 'photo']