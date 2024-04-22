from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from main.models import Gasto


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(), label='Usuario')
    password = forms.CharField(widget=PasswordInput(), label='Senha')


class CadastroForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(widget=PasswordInput(), label='Senha')
    password2 = forms.CharField(
        widget=PasswordInput(), label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class GastoForm(ModelForm):

    class Meta:
        model = Gasto
        fields = ['nome', 'descricao', 'valor', 'categoria']
